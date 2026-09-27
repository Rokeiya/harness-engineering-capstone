from pathlib import Path

from claims_intake.run import _run_one, _summary_row
from tests.fakes import FakeBlock, FakeClient, FakeMessages, FakeResponse, FakeUsage


def test_end_turn_without_terminal_tool_escalates(tmp_path: Path) -> None:
    client = FakeClient(
        messages=FakeMessages(
            scripted=[
                FakeResponse(
                    content=[FakeBlock(type="text", text="I have finished.")],
                    stop_reason="end_turn",
                    usage=FakeUsage(input_tokens=10, output_tokens=5),
                )
            ]
        )
    )

    result = _run_one(
        client=client,
        model="fake-model",
        fixture={
            "claim_id": "claim_test",
            "policy_id": "POL-1",
            "initial_message": "Please process this claim.",
        },
        policies={},
        run_dir=tmp_path,
        max_input_tokens=1_000,
        max_wall_clock_s=60.0,
    )

    assert result.state is not None
    assert result.session.outcome == "escalated"
    assert result.session.escalation is not None
    assert result.session.escalation["reason"] == "missing_terminal_tool"
    assert (tmp_path / "escalations.jsonl").exists()
    assert _summary_row("fake-model", result)["claim_type"] == "-"