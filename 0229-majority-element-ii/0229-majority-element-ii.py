from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3
        counts = Counter(nums)
        
        return [num for num, count in counts.items() if count > threshold]
        