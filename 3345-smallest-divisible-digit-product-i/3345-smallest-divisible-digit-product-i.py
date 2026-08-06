class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            prod = 1
            for digit in str(n):
                prod *= int(digit)
            
            if prod % t == 0:
                return n
            
            n += 1