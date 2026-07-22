class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = 0
        for i in range(len(word)):
            if ch == word[i]:
                index = i
                break
        return word[index::-1] + word[index + 1:len(word):1]       

                      

        