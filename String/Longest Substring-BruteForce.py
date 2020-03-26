def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            substring = ''
            subllongest = 0
            for j in range(i, len(s)):
                if substring.find(s[j]) ==-1:
                    substring = substring + s[j]
                    subllongest = subllongest + 1
                else:
                    break
            if subllongest>longest:
                longest = subllongest
        return longest
                    
