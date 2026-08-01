class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}

        def maxDiff(i: int, j: int) -> int:
            if i == j:
                return nums[i]
            
            if (i, j) in memo:
                return memo[(i, j)]

            # Option 1: Take nums[i]
            pick_left = nums[i] - maxDiff(i + 1, j)
            # Option 2: Take nums[j]
            pick_right = nums[j] - maxDiff(i, j - 1)

            memo[(i, j)] = max(pick_left, pick_right)
            return memo[(i, j)]

        # If Player 1's final score difference >= 0, Player 1 wins
        return maxDiff(0, len(nums) - 1) >= 0