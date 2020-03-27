def reverse(self, x: int) -> int:
        negative = 0
        if x<0:
            negative = 1
        if x>=0:
            a = str(x)
            b = ''
            for i in range(1,1 + len(a)):
                b = b + a[-i]
            b = int(b)
        if x<0:
            a = str(x)
            b = ''
            for i in range(1, len(a)):
                b = b + a[-i]
            b = -1 * int(b)
        if (b< -2**31) or b> (2**31-1):
            return 0
        return b
