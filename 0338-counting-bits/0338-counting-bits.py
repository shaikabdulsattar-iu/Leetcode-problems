class Solution:
    def countBits(self, n: int) -> List[int]:
        a = [0]
        k = 0

        while len(a) <= n:
            new_a = [0] * (2**k)
            for i in range(2**k):
                new_a[i] = a[i] + 1
            a = a + new_a
            k += 1
            
        return a[:n+1]
        