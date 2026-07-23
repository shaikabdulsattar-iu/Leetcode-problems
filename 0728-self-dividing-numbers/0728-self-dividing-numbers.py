class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right + 1):
            temp = num
            is_self_div = True
            while temp > 0:
                digit = temp % 10
                if digit == 0 or num % digit != 0:
                    is_self_div = False
                    break
                temp //= 10
            
            if is_self_div:
                res.append(num)      
        return res       

                


        