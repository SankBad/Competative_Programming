class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        no1 = 0
        no2 = 0
        for i in range(len(num1)-1,-1,-1):
            no1 =  no1+(10**(len(num1)-1-i))*int(num1[i])
        
        for j in range(len(num2)-1,-1,-1):
            no2 = no2+(10**(len(num2)-1-j))*int(num2[j])
        return str(no1+no2)
