class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res =0
        for x in nums:
            res |= x
        return res*(2**(len(nums)-1))
        
        