class Solution:
    def defangIPaddr(self, address: str) -> str:
        l = []
        for i in address:
            if i == ".":
                l.append("[.]")
            else:
                l.append(i)    
        return "".join(l)


        