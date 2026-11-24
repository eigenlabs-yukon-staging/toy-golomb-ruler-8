# Starting submission: length 127

Marks: 0, 1, 3, 7, 15, 31, 63, 127 (each is 2^k − 1).

Every pairwise difference is (2^j − 1) − (2^i − 1) = 2^i (2^(j−i) − 1) with i < j. The factor 2^i fixes i and the odd factor 2^(j−i) − 1 then fixes j, so no two pairs share a difference. The ruler is valid and its length is 127, far from the best known 34: there is a lot of room to improve.
