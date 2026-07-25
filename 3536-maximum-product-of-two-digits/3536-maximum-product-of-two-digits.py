class Solution:
    def maxProduct(self, n: int) -> int:
        n1=list(str(n))
        n1.sort()
        return int(n1[-1])*int(n1[-2])
       
        

            
        