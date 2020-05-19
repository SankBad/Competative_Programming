class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l = 0
        r = len(A)-1
        while(l<=r):
            if A[l]%2==0:
                l = l+1
                continue
            else:
                temp=A[r]
                A[r]=A[l]
                A[l]=temp
                r = r-1
        return A
