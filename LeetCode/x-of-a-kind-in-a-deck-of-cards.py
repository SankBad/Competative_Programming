class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from fractions import gcd
        from functools import reduce
        mydict = {}
        for i in deck:
            if i not in mydict:
                mydict[i] = 1
            else:
                mydict[i] = mydict[i]+1
        mylist = []
        for i in mydict:
            mylist.append(mydict[i])
            
        gcd_val= reduce(gcd, mylist)
        return gcd_val>=2
            
        
