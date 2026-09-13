class Solution:
    def passwordStrength(self, password: str) -> int:
        l1 = list(set(password))
        sum_ = 0
        for i in l1:
            if i in 'qwertyuioplkjhgfdsazxcvbnm':
                sum_ = sum_ + 1
            elif i in 'QWERTYUIOPLKJHGFDSAZXCVBNM':
                sum_ = sum_ + 2
            elif i in '1234567890':
                sum_ = sum_ + 3
            else:
                sum_ = sum_ + 5
        return sum_                
                    

        