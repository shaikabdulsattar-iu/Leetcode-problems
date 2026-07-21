class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1: Strip leading whitespaces
        s = s.lstrip()
        if not s:
            return 0
        
        # Step 2: Handle sign
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
            
        # Step 3: Extract digits
        num = 0
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1
            
        # Step 4: Apply sign and clamp to 32-bit signed int range [-2^31, 2^31 - 1]
        num *= sign
        return max(-2**31, min(2**31 - 1, num))