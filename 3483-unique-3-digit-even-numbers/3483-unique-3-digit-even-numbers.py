from itertools import permutations
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        numbers = set()

        for a, b, c in permutations(digits, 3):
            if a != 0 and c % 2 == 0:
                numbers.add(100 * a + 10 * b + c)

        return len(numbers)




        