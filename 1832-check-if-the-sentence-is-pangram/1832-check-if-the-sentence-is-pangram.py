class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        c = set(sentence)
        if len(c) == 26:
            return True
        else:
            return False    
        