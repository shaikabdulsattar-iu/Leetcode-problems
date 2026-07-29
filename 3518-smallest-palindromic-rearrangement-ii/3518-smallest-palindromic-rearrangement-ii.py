from collections import Counter
import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        freq = Counter(s)
        
        mid_char = ""
        half_counts = {}
        for char, count in sorted(freq.items()):
            if count % 2 == 1:
                mid_char = char
            half_counts[char] = count // 2
            
        half_len = n // 2

        # Helper function to compute total unique permutations capped at cap
        def count_permutations(counts, cap):
            total_len = sum(counts.values())
            res = 1
            curr_len = total_len
            
            for char, count in counts.items():
                if count == 0:
                    continue
                # Calculate C(curr_len, count)
                res *= math.comb(curr_len, count)
                if res > cap:
                    return cap + 1
                curr_len -= count
                
            return res

        # Check if k exceeds total valid permutations
        if count_permutations(half_counts, k) < k:
            return ""

        # Build the lexicographically smallest half
        first_half = []
        for _ in range(half_len):
            for char in sorted(half_counts.keys()):
                if half_counts[char] == 0:
                    continue
                
                # Try picking 'char'
                half_counts[char] -= 1
                ways = count_permutations(half_counts, k)
                
                if ways >= k:
                    first_half.append(char)
                    break
                else:
                    k -= ways
                    half_counts[char] += 1  # Backtrack

        first_half_str = "".join(first_half)
        return first_half_str + mid_char + first_half_str[::-1]