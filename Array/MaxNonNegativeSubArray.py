#https://www.interviewbit.com/problems/max-non-negative-subarray/
def maxset(A):
        SumArr = {}
        N = len(A)
        i = 0
        while (i<N):
            #print(i)
            SumArr[i] = 0
            j = i
            while(A[j]>=0):
                SumArr[i] = SumArr[i] + A[j]
                j += 1
                if j==N:
                    break
            i = j+1
        
        maxvalue = -sys.maxsize
        for i, j in SumArr.items():
            if j>maxvalue:
                maxindex = i
                maxvalue = j
                
        ReturnArr = []
        i = maxindex
        while(A[i]>=0):
            ReturnArr.append(A[i])
            i += 1
            if i>=N:
                break
        return ReturnArr
    
A = [ 756898537, -1973594324, -2038664370, -184803526, 1424268980 ]
print(maxset(A))
