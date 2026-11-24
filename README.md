# Golomb Ruler 8 (toy challenge)

Place 8 marks on a ruler, starting at 0, so that no two pairs of marks are the same distance apart. Make the ruler as short as you can. The score is the ruler's length; lower is better.

- [`rules.md`](rules.md): the exact definition, the score, and what does not count.
- [`submission/`](submission): the only directory you edit. It starts at length 127.
- [`checkers/golomb_gate.py`](checkers/golomb_gate.py): the protected check that decides validity and the score.

## Submit a ruler

1. Put your 8 marks in `submission/submission.json` under the `golomb_gate` check's `marks`.
2. State the same marks and length in the claim, and update `submission/proof.md`.
3. Run `llm-verifier check --root .`, then submit.

<!-- llm-verifier:solver-guidance:begin -->
## Preparing a submission

Read the [solver guide](https://github.com/Layr-Labs/llm-verifier/blob/939a35dbb233c062ae514bd9abc62d3168eba1fc/docs/solving.md) and
[solver skill](https://github.com/Layr-Labs/llm-verifier/blob/939a35dbb233c062ae514bd9abc62d3168eba1fc/skills/llm-verifier-solver/SKILL.md)
from the same pinned verifier revision as this challenge.

- Use the challenge's verifier revision for `llm-verifier check --root .`.
- Run the final submission's declared computations through `intake`,
  `prepare-runtime`, and `experiments` without model credentials.
  `test-checkers` runs organizer fixtures, not your candidate's checks.
- Ask a fresh independent subagent to critique the complete final submission,
  protected rules, selected policies and evidence using the guide.
- Fix findings and rerun affected checks and review.
- Report results and omitted steps. Subagent critique is advisory;
  configured-provider review is separate. `simulate` does not judge correctness.
<!-- llm-verifier:solver-guidance:end -->
