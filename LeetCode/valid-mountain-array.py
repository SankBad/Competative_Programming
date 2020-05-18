class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        val = 1
        First = 0
        Second = 0
        for i in range(len(A)-1):
            if (A[i+1]-A[i])  >0 and val:
                First = 1
                continue
            elif A[i+1]-A[i] <0:
                Second = 1
                val = 0
                continue
            else:
                return False
        return (First and Second)
