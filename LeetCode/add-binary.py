class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num = int(a, 2) + int(b, 2)
        return '{0:b}'.format(num)
