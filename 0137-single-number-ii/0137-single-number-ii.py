class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num]+=1
        
        for key,value in freq.items():
            if value==1:
                return key
        