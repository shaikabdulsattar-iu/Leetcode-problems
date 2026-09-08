class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        p = 1
        while n > 4:
            p *= 3
            n -= 3
        p *= n
        return p            
        