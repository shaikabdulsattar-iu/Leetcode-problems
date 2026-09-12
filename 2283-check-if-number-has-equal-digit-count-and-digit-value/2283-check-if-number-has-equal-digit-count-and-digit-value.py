from collections import Counter
class Solution:
    def digitCount(self, num: str) -> bool:
        counts = Counter(num)
        for i in range(len(num)):
            if counts[str(i)] != int(num[i]):
                return False
        return True          
        