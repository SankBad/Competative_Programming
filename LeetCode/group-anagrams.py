class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        for i in strs:
            if tuple(sorted(i)) not in mydict:
                mydict[tuple(sorted(i))] = [i]
            else:
                mydict[tuple(sorted(i))].append(i)
                
        return list(mydict.values())
