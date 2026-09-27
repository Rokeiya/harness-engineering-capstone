# Evidence Index

## System 1: Claims Intake Agent

- Required test log: `evidences/system_1_claims_loop/tests.txt` (29 passed)
- Supplemental complete test log: `evidences/system_1_claims_loop/tests_all.txt` (30 passed, including the fallback regression)
- Run artifact: `evidences/system_1_claims_loop/run_summary.md`
- Trace: `evidences/system_1_claims_loop/trace.jsonl`
- Cost and run metrics: `run_summary.md`; reflection Part 1, questions 1-4

## System 2: Context Strategy

- Required test log: `evidences/system_2_context_strategy/tests_required.txt` (17 passed)
- Submitted full-suite log: `evidences/system_2_context_strategy/tests.txt` (30 passed in the original Linux/Python 3.13 environment)
- Current full-suite recheck: `evidences/system_2_context_strategy/tests_recheck.txt` (28 passed, 2 artifact-dependent skips)
- Budget: `evidences/system_2_context_strategy/budget.json`
- Evaluation: `evidences/system_2_context_strategy/eval.jsonl` and `eval_control.jsonl`
- Reflection: Part 1, questions 5-7

## System 3: Claude Code Configuration

- Required test log: `evidences/system_3_claude_config/tests.txt` (35 passed)
- Validation output: `evidences/system_3_claude_config/validator.txt`
- Configuration artifacts: `evidences/system_3_claude_config/CLAUDE.md` and `.claude/`
- Reflection: Part 1, questions 8-10

## System 4: Orchestration

- Required test log: `evidences/system_4_orchestration/tests_required.txt` (28 passed)
- Supplemental complete test log: `evidences/system_4_orchestration/tests.txt` (33 passed)
- Shift run: `evidences/system_4_orchestration/shift_run.md`
- Fork evidence: `evidences/system_4_orchestration/fork_evidence.md`
- Hot-state size: `evidences/system_4_orchestration/hot_state_size.txt`
- Reflection: Part 1, questions 11-13

## Cross-System

- Required suite counts together: `evidences/verification.txt`
- Reflection synthesis and honest assessment: `evidences/reflection.md`, Part 2 and Part 3