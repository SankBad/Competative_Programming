class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = str(n)
        b = 1
        c = 0
        for i in a:
            b = b*int(i)
            c = c + int(i)
        return b-c
