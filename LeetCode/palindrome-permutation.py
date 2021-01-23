from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter_dict = Counter(s)
        trig  = 0
        for i in counter_dict.values():
            if i%2==0:
                continue
            else:
                trig += 1
                if trig>1:
                    return False
        return True
