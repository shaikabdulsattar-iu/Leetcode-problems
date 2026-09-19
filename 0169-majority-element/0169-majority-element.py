from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        s = Counter(nums)
        for i,j in s.items():
            if j > len(nums)//2:
                return i

        