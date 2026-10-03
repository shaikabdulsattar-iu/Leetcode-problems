class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        l = []
        nums2_copy = list(nums2)
        
        for i in nums1:
            for j in nums2_copy:
                if i == j:
                    l.append(i)
                    nums2_copy.remove(j)  
                    break                 
                    
        return l