class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            for j in range(2,int(n**0.5)+1):
                if n%j==0:
                    return False
            return True
        for count in d.values():
            if is_prime(count):
                return True
        return False                       