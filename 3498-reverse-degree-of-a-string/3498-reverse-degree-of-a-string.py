class Solution:
    def reverseDegree(self, s: str) -> int:
        degree = 0
        num = 0
        for i in range(len(s)):
            num = 123 - ord(s[i])
            degree += num * (i+1)
        
        return degree