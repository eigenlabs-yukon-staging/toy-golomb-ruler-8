"""Organizer-owned gate for Golomb Ruler 8.

Reads {"marks": [...]} from stdin and prints one JSON object. It passes only when
the marks are exactly 8 distinct integers in strictly increasing order, the first
is 0, every mark is at most 1000, and all 28 pairwise differences are different.
On a pass it reports ruler_length, the largest mark. It is pure arithmetic.
"""
import json
import sys

N = 8
MAX_MARK = 1000


def judge(marks):
    if not isinstance(marks, list) or len(marks) != N:
        return False, "need exactly 8 marks"
    if any(type(m) is not int for m in marks):
        return False, "every mark must be an integer"
    if marks[0] != 0:
        return False, "the first mark must be 0"
    if any(b <= a for a, b in zip(marks, marks[1:])):
        return False, "marks must be strictly increasing"
    if marks[-1] > MAX_MARK:
        return False, "marks must be at most 1000"
    seen = {}
    for i in range(N):
        for j in range(i + 1, N):
            d = marks[j] - marks[i]
            if d in seen:
                a, b = seen[d]
                return False, "difference %d repeats: %d-%d and %d-%d" % (
                    d, marks[b], marks[a], marks[j], marks[i])
            seen[d] = (i, j)
    return True, "all 28 pairwise differences are distinct"


inputs = json.load(sys.stdin)
marks = inputs.get("marks")
passed, message = judge(marks)
print(json.dumps({
    "passed": passed,
    "ruler_length": marks[-1] if passed else 0,
    "message": message[:128],
}, ensure_ascii=True))
