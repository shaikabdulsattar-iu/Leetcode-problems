class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        l = max(nums)
        idx = nums.index(l)
        nums.remove(l)
        for i in nums:
            if i*2 > l:
                return -1
        return idx        
        