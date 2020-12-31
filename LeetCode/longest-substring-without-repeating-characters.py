class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        l = 0
        r = 1
        curr = 0
        currmax = 0
        while(r<len(s)):
            if s[r] not in s[l:r]:
                r=r+1
            else:
                if currmax<r-l+1:
                    currmax = r-l
                l = l+1
                r = l+1
        curmax1 = r-l
        return max(currmax, curmax1)
