from collections import Counter
from typing import List


class Solution:

  def totalNumbers(self, digits: List[int]) -> int:
    c = Counter(digits)
    return sum(
        all(c[d] >= cnt for d, cnt in Counter(map(int, str(n))).items())
        for n in range(100, 1000, 2)
    )