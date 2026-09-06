class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        a_c = []
        b_c = []
        for i in range(1,a+1):
            if a % i == 0:
                a_c.append(i)
        for j in range(1,b+1):
            if b % j == 0:
                b_c.append(j)
        return len(set(a_c) & set(b_c))        