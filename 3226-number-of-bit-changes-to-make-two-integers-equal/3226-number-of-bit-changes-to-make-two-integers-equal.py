class Solution:

  def minChanges(self, n: int, k: int) -> int:
    # If k has any 1-bit that n does not have, it's impossible
    if (n & k) != k:
      return -1

    # Count how many 1s in n need to be flipped to 0
    return (n ^ k).bit_count()