class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        half_len = n // 2
        
        # Sort the characters of the left half
        left_half = "".join(sorted(s[:half_len]))
        
        # Build the palindrome based on parity
        if n % 2 == 0:
            return left_half + left_half[::-1]
        else:
            return left_half + s[half_len] + left_half[::-1]