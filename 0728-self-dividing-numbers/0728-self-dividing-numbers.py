class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        for i in range(left, right + 1):
            n = i

            while n != 0:
                divisor = n % 10

                if divisor == 0 or i % divisor != 0:
                    break

                n //= 10

            if n == 0:
                res.append(i)
                
        return res
        