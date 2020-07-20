class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        b=0
        if n>0:
            while(n!=1 and b ==0):
                n, b = divmod(n,2)
        if n<=-1:
            return False
        if n<0:
            n = -1/n
            while(n!=1 and b ==0):
                n, b = divmod(n,2)
        
        if n==1:
            return True
        else:
            return False
