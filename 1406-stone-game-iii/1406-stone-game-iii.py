from functools import cache
from typing import List


class Solution:

  def stoneGameIII(self, stoneValue: List[int]) -> str:
    n = len(stoneValue)

    @cache
    def maxDiff(i: int) -> int:
      if i == n:
        return 0

      # Try taking 1, 2, or 3 stones
      ans = float("-inf")
      current_sum = 0

      for k in range(1, 4):
        if i + k <= n:
          current_sum += stoneValue[i + k - 1]
          ans = max(ans, current_sum - maxDiff(i + k))

      return ans

    alice_diff = maxDiff(0)

    if alice_diff > 0:
      return "Alice"
    elif alice_diff < 0:
      return "Bob"
    else:
      return "Tie"       
        