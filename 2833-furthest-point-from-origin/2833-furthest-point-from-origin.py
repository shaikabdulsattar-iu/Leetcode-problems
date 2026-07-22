class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = 0
        r = 0
        b = 0
        for i in range(len(moves)):
            if  moves[i] == 'L':
                l = l-1
            elif moves[i] == 'R':
                r = r+1
            else:
                b = b+1
        return abs(l+r)+b                 
        