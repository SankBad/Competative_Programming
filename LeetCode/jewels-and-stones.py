class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        total = 0
        from collections import Counter
        myDict = dict(Counter(S))
        for i in myDict:
            if i in J:
                total += myDict[i]
        return total
