class Solution:
    def addDigits(self, num: int) -> int:
        while(len(str(num))!=1):
            num1 = 0
            for i in str(num):
                num1 = num1 + int(i)
            num = num1
        return num
