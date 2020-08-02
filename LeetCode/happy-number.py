class Solution:
    def isHappy(self, n: int) -> bool:
        Happy_list = []
        if n<1:
            return False
        while(n!=1 and n not in Happy_list):
            Happy_list.append(n)
            new_n = 0
            for i in str(n):
                new_n += int(i)**2
            n = new_n
        
        if n==1:
            return True
        else:
            return False
