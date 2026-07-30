class Solution:
    def canWinNim(self, n: int) -> bool:
        return n < 4 or n % 4 != 0