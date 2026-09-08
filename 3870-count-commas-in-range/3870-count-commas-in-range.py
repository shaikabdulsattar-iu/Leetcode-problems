class Solution:
    def countCommas(self, n: int) -> int:
        l = []
        if n < 1000:
            return 0
        for i in range(1000,n+1):
            l.append(i)
        return len(l)    
