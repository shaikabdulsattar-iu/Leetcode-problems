class Solution:
    def findGCD(self, nums: list[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        l = []
        for i in range(1,mn+1):
            if mn%i==0 and mx%i==0:
                l.append(i)
        return max(l)
        