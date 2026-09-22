from collections import Counter
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        l = 0
        feq = Counter(nums)
        for i ,j in feq.items():
            if j % k == 0:
                l += j * i
        return l           


        