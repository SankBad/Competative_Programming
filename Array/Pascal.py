#https://www.interviewbit.com/problems/kth-row-of-pascals-triangle/
def solve(A):
        SolArr = [[0 for x in range(A+1)] for y in range(A+1)]
        SolArr[1][1]=1
        for i in range(2, A+1):
            for j in range(1, i+1):
                SolArr[i][j] = SolArr[i-1][j] + SolArr[i-1][j-1]
        
        SolArr1 = [[0 for x in range(y+1)] for y in range(A)]
        for i in range(A):
            for j in range(i+1):
                SolArr1[i][j] = SolArr[i+1][j+1]
                
        return SolArr1
