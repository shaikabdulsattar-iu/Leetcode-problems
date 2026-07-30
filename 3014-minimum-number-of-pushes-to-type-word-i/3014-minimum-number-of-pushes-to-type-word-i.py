class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        p = 0
        for i in range(n):
            p += (i//8) + 1
        return p    
        