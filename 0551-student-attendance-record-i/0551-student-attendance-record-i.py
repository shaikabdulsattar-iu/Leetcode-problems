from collections import Counter
class Solution:
    def checkRecord(self, s: str) -> bool:
        S = Counter(s)
        return S['A'] < 2 and "LLL" not in s


        