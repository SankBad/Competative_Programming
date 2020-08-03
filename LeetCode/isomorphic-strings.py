class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen = []
        for i in range(len(s)):
            if s[i] in seen:
                continue
            else:
                t = t[:i] + t[i:].replace(t[i], s[i])
                seen.append(s[i])
        return t==s
