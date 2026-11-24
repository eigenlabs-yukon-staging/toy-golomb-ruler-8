# Golomb Ruler 8

Find a Golomb ruler with 8 marks that is as short as you can make it.

## Problem and model

A Golomb ruler with 8 marks is a list of 8 integers `0 = a1 < a2 < … < a8` such that the 28 differences `aj − ai` (for `i < j`) are all different. Its length is `a8`, the largest mark. Marks must be at most 1000.

## Score

The score is the length `a8`. Lower is better. The best length known (and proved optimal) for 8 marks is 34; the starting submission has length 127. Scores are whole numbers between 28 and 1000.

## What does not count

- Fewer or more than 8 marks.
- A list that does not start at 0, is not strictly increasing, or has a non-integer mark.
- Any repeated difference, however the submission argues around it.
- A length stated in prose or in the claim that is not the largest mark the check received.

## Submission and review

Edit only `submission/`. Put your marks in the `golomb_gate` check inputs in `submission/submission.json`, state the same marks and length in the claim, and say briefly in `proof.md` how you found them. The protected checker `checkers/golomb_gate.py` decides validity and the score by arithmetic alone; a reviewer model confirms the claim matches the checked marks. Results are promoted automatically.
