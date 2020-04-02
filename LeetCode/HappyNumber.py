class Solution:
    def isHappy(self, n: int) -> bool:
        IsCycle = []
        IsCycle.append(n)
        number = str(n)
        while(n!=1):
            number = str(n)
            n=0
            for i in number:
                n = n + int(i)**2
            if n in IsCycle:
                return False
            else:
                IsCycle.append(n)                
        return True
