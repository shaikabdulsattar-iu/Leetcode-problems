class Solution:

  def stoneGameIII(self, stoneValue: list[int]) -> str:
    n = len(stoneValue)
    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
      dp[i] = float("-inf")
      current_sum = 0
      for k in range(1, 4):
        if i + k <= n:
          current_sum += stoneValue[i + k - 1]
          dp[i] = max(dp[i], current_sum - dp[i + k])

    alice_diff = dp[0]

    if alice_diff > 0:
      return "Alice"
    elif alice_diff < 0:
      return "Bob"
    else:
      return "Tie"