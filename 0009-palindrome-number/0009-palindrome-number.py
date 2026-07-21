class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = str(x)
        return n == n[::-1]
       
