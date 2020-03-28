class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringint = str(x)
        if stringint[0] == '-':
            return False
        elif stringint[::-1] == stringint:
            return True
