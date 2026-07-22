class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sr = s.split()
        return len(sr[-1])
        