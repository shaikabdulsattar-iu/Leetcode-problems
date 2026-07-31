class Solution:
    def reverseBits(self, n: int) -> int:
        s = f"{n:032b}"
        rev = s[::-1]
        return int(rev,2)
    
        