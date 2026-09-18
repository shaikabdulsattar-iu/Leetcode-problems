from collections import Counter
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        s = Counter(nums)
        for key,values in s.items():
            if values == 1:
                return key
        