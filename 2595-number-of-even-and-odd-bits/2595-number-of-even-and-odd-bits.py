class Solution:

  def evenOddBit(self, n: int) -> list[int]:
    even = 0
    odd = 0
    idx = 0

    while n > 0:
      if n & 1:
        if idx % 2 == 0:
          even += 1
        else:
          odd += 1
      n >>= 1
      idx += 1

    return [even, odd]