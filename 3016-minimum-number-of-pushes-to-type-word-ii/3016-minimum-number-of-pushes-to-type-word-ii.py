from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Step 1: Count frequency of each character
        counts = Counter(word)
        
        # Step 2: Sort frequencies in descending order
        sorted_freqs = sorted(counts.values(), reverse=True)
        
        # Step 3: Calculate minimum pushes
        total_pushes = 0
        for i, freq in enumerate(sorted_freqs):
            pushes_needed = (i // 8) + 1
            total_pushes += freq * pushes_needed
            
        return total_pushes
        