class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        m = 1 << n
        res = []
        for i in range(0,m):
            ans = []
            for j in range(n):
                if i & (1 << j) > 0:
                    ans.append(nums[j])
            res.append(ans)        
        return res        
        