class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_pro = 1
        sum_add = 0
        while n > 0:
            dig = n%10
            sum_pro = sum_pro*dig
            sum_add = sum_add+dig
            n //= 10
        return sum_pro - sum_add    
        