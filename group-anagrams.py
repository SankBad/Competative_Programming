
from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict =  defaultdict(list)
        for i in strs:
            j = i
            i = "". join(sorted(i))
            my_dict[i].append(j)
        
        ans = []
        for i in my_dict.values():
            ans.append(i)
        
        return ans
