class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1 
        temp = self.myPow(x, int(n/2))
        if int(n%2)==0:
            return temp* temp
        elif n>0:
            return (x * temp* temp)
        else:
            return (1/x * temp* temp)
