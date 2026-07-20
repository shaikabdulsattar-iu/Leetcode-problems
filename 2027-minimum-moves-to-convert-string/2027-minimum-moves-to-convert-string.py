class Solution:
    def minimumMoves(self, s: str) -> int:
        ans=i=0
        while i<len(s):
            if s[i]=='O':i+=1
            else:
                i+=3
                ans+=1
        return ans
        