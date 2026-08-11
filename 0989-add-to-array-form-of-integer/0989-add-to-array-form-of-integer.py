class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res = []
        i = len(num) - 1  # Start at the last index of num (index 2)
        
        while i >= 0 or k > 0:
            if i >= 0:
                k += num[i]  # Add current digit of num to k
                i -= 1       # Move one position left
            
            res.append(k % 10)  # Store the last digit of total sum
            k //= 10            # Keep the carry for the next position
            
        return res[::-1]  # Reverse to get the final correct order