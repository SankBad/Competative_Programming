class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        length = len(s)
        if length==0:
            return True
        j = 0
        for i in t:
            if i==s[j]:
                j = j+1
            if j==length:
                return True
        return False
