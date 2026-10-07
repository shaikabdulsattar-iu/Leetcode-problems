class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        l = set(nums1)
        l1 = set(nums2)
        l2 = []
        for i in l:
            for j in l1:
                if i == j:
                    l2.append(i)
        return l2            
        