class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        b=0
        if n>0:
            while(n!=1 and b ==0):
                n, b = divmod(n,2)
        if n<=0:
            return False
        
        
        if (n==1 and b==0):
            return True
        else:
            return False
