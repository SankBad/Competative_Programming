# addition of digits until you get single digit

def DigitOne(n):
    while(int(n)>9):
        string = str(n)
        n = 0
        for i in string:
            n += int(i)
    return n

t=int(input())
for i in range(t):
    a=int(input())
    print(DigitOne(a))
