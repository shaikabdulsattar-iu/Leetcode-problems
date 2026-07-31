class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = set()
        for i in nums1:
            for j in nums2:
                if i == j:
                    l.add(i)
        return list(l)            

        