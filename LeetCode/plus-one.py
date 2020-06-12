class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        output = []
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            val = digits[i]+carry
            carry, rem = divmod(val,10)
            output.append(rem)
        if carry !=0:
            output.append(carry)
        output.reverse()
        return output
