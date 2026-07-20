class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            total_sum = 0
            while n > 0:
                digit = n % 10
                total_sum += digit * digit
                n //= 10 
            
            n = total_sum
            
        return n == 1