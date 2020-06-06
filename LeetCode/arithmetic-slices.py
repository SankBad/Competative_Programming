class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        total = 0
        num = 0
        if len(A)<=2:
            return 0
        d = A[1]-A[0]
        for i in range(len(A)-1):
            if A[i+1]-A[i]==d:
                num = num+1
            else:
                if num>=2:
                    total += int((num-1)*(num)/2)
                num = 1
                d = A[i+1]-A[i]
        if num>=2:
            total += int((num-1)*(num)/2)
        return total
