class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        min_val, max_val = min(nums), max(nums)
        return [x for x in range(min_val, max_val + 1) if x not in num_set]


        