class Solution:
    def __init__(self):
        self.my_dict = {}
        
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.wb_utility(s, wordDict, 0)
        
    def wb_utility(self, s, wordDict, start):
        first = False
        if start==len(s):
            return True
        for end in range(start+1, len(s)+1):
            if end not in self.my_dict:
                self.my_dict[end] = self.wb_utility(s, wordDict, end)
            if s[start:end] in wordDict and self.my_dict[end]:
                return True
        return False
