class Solution:
    def countCommas(self, n: int) -> int:
        l1 = []
        for i in range(1000,n+1):
            l1.append(i)
        return len(l1)    
        