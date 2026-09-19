class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        rev = 0
        for i in s+t:
            rev ^= ord(i)
        return chr(rev)    

        