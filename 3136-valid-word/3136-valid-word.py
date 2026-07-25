class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        
        vowels = set("aeiouAEIOU")
        _vowel = False
        _consonant = False
        
        for i in word:
            if not i.isalnum():
                return False
            if i in vowels:
                _vowel = True
            elif i.isalpha(): 
                _consonant = True
        return _vowel and _consonant             
        

        