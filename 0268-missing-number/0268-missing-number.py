class Solution:

  def missingNumber(self, nums: list[int]) -> int:
    l = len(nums) + 1
    l1 = []
    for i in range(0, l):
      l1.append(i)

    combined = l1 + nums
    res = 0
    for x in combined:
      res ^= x
    return res  

        