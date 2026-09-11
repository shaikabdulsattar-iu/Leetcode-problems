from collections import Counter

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        available = Counter(digits)
        count = 0
        
        for num in range(100, 1000, 2):
            h = num // 100
            t = (num // 10) % 10
            o = num % 10
            
            needed = Counter([h, t, o])
            
            if all(available[d] >= needed[d] for d in needed):
                count += 1
                
        return count


        