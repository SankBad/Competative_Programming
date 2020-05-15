class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A)-1
        output = [0]*len(A)
        n = len(A)-1
        while(i<=j):
            if A[i]**2 < A[j]**2:
                output[n]= A[j]**2
                j = j -1
            else:
                output[n]= A[i]**2
                i = i + 1
            n = n -1
        return output
