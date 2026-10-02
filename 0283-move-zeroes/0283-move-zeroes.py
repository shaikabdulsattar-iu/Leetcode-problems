class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        l = []
        while 0 in nums:
            nums.remove(0)
            l.append(0)
        nums.extend(l)            
        