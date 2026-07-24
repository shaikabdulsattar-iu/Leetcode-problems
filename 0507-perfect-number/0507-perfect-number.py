class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        total_sum = 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                total_sum += i
                if i * i != num:
                    total_sum += num // i
            i += 1
            
        return total_sum == num       



        
        