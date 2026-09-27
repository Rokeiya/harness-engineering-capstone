# Run summary — 20260922_121649

- Model: `claude-haiku-4-5-20251001`
- Fixtures processed: 8
- Estimated total cost: **$0.1127** USD
- Missing-terminal outcomes are escalated by the harness fallback.

> Evidence note: The five normally stopped claims below are marked escalated under the current fallback. Token and latency figures are retained from the recorded run; a live API rerun was unavailable because `ANTHROPIC_API_KEY` is not configured in this environment.

| claim_id | outcome | claim_type | severity | turns | clarifications_asked | input_tokens | output_tokens | est_cost_usd | elapsed_s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| claim_01_kitchen_fire | escalated | - | - | 2 | 0 | 6380 | 511 | 0.0089 | 5.2 |
| claim_02_stolen_bike | escalated | - | - | 2 | 0 | 6158 | 444 | 0.0084 | 4.3 |
| claim_03_water_damage | routed | property_damage | high | 7 | 1 | 25442 | 1180 | 0.0313 | 14.9 |
| claim_04_neighbor_injury | escalated | - | - | 2 | 0 | 6182 | 469 | 0.0085 | 4.7 |
| claim_05_auto_collision | routed | auto | high | 4 | 0 | 14960 | 975 | 0.0198 | 10.7 |
| claim_06_low_confidence_escalation | escalated | - | - | 2 | 0 | 5827 | 297 | 0.0073 | 4.4 |
| claim_07_tree_falls_on_car | escalated | - | - | 2 | 0 | 6413 | 643 | 0.0096 | 5.7 |
| claim_08_minor_porch_damage | routed | property_damage | low | 4 | 0 | 14430 | 869 | 0.0188 | 10.2 |
