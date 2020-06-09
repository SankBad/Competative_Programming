class Solution:
    def isUgly(self, num: int) -> bool:
        if num<=0:
            return False
        if num==1:
            return True
        if num%5==0:
            return self.isUgly(num/5)
        elif num%3==0:
            return self.isUgly(num/3)
        elif num%2==0:
            return self.isUgly(num/2)
        else:
            return False
