class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            num = len(str(i))
            if num % 2 == 0:
                count += 1
        return count        

        