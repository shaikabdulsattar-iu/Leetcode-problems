class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        s = bin(n)[2:][::-1]
        l = []
        e = 0
        o = 0
        for i in range(len(s)):
            if s[i] == '1':
                l.append(i)
        for i in l:
            if i%2 == 0:
                e += 1
            else:
                o += 1
        return [e,o]            




        