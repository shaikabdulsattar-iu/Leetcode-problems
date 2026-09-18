class Solution:
    def romanToInt(self, s: str) -> int:
        s = (
            s.replace("IV", "a")
            .replace("IX", "b")
            .replace("XL", "c")
            .replace("XC", "d")
            .replace("CD", "e")
            .replace("CM", "f")
        )

        sum_ = 0
        for i in s:
            if i == "a":
                sum_ += 4
            elif i == "b":
                sum_ += 9
            elif i == "c":
                sum_ += 40
            elif i == "d":
                sum_ += 90
            elif i == "e":
                sum_ += 400
            elif i == "f":
                sum_ += 900
            elif i == "I":
                sum_ += 1
            elif i == "V":
                sum_ += 5
            elif i == "X":
                sum_ += 10
            elif i == "L":
                sum_ += 50
            elif i == "C":
                sum_ += 100
            elif i == "D":
                sum_ += 500
            elif i == "M":
                sum_ += 1000

        return sum_