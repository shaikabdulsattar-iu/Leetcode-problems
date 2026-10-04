class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            # ans[i >> 1] is the bit count of i // 2
            # (i & 1) checks if the least significant bit is 1
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
        
        