#https://www.interviewbit.com/problems/sorted-insert-position/
def searchInsert(self, A, B):
        l = 0
        r = len(A)-1
        while(l<=r):
            mid = l + (r-l)//2
    
            if A[mid]==B:
                return mid
            elif A[mid]>B:
                if mid-1>-1:
                    if B>A[mid-1]:
                        return mid 
                    else:
                        r = mid-1
                else:
                    break
            else:
                if mid+1<len(A):
                    if B<A[mid+1]:
                        return mid+1
                    else:
                        l = mid+1
                else:
                    break
        if B>A[0]:
            return len(A)
        else:
            return 0
    
A = [ 1, 3, 5, 6 ]
B = 7
searchInsert(A, B)
