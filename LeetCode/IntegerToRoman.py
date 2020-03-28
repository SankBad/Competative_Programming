class Solution:
    def intToRoman(self, num: int) -> str:
        output = ''
        mydict = { 1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10: 'X', 9: 'IX', 5:'V', 4: 'IV', 1: 'I'}
        for a, b in mydict.items():
            if num//a>0:
                c, num = divmod(num, a)
                output = output + c*b
        return output
