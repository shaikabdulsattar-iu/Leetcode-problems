class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1 = nums[:n]
        l2 = nums[n:]
        new = []
        for i in range(n):
            new.append(l1[i])
            new.append(l2[i])
        return new

        