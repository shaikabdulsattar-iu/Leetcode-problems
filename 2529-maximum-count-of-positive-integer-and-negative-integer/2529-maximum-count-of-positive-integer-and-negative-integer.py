class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        e_c  = 0
        o_c = 0
        for i in nums:
            if i > 0:
                e_c += 1
            elif i < 0:
                o_c += 1       
        return max(e_c,o_c)