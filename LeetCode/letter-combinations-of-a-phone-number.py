class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        ans_arr  = []
        if len(digits)==0:
            return ans_arr
        self.utility(digits, ans_arr, phone, '')
        return ans_arr
    
    def utility(self, digits, ans_arr, phone, comb):
        if len(digits)==0:
            return ans_arr.append(comb)
        else:
            for i in phone[digits[0]]:
                self.utility(digits[1:], ans_arr, phone, comb+i)
            
