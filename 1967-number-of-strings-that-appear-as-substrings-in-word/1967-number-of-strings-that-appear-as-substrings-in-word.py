class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
            return sum(1 for i in patterns if i in word)
        