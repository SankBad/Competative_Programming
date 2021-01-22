class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        ans = ''
        for i in range(len(s)):
            p = i-1
            q = i+1
            while(p>-1 and q<len(s)):
                if s[p]==s[q]:
                    p -= 1
                    q += 1
                else:
                    break
            if longest<q-p:
                longest = q-p
                ans = s[p+1:q]
                
        for i in range(len(s)):
            p = i
            q = i+1
            while(p>-1 and q<len(s)):
                if s[p]==s[q]:
                    p -= 1
                    q += 1
                else:
                    break
            if longest<q-p:
                longest = q- 1-p+1
                ans = s[p+1:q]
            
        return ans
