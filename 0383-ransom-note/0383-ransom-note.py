from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_count = Counter(ransomNote)
        mag_count = Counter(magazine)
        return note_count <= mag_count
        