class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        total = 0
        threshold = 1000
        while n >= threshold:
            total += n - threshold + 1
            threshold *= 1000
        return total       

        