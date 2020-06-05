class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        if rows==0:
            return False
        cols = len(matrix[0])
        total = rows*cols
        l = 0
        r = total-1
        while(l<=r):
            mid = l + (r-l)//2
            p = mid//cols
            q = mid%cols-1
            if matrix[p][q]==target:
                return True
            elif matrix[p][q]>target:
                r = mid-1
            else:
                l = mid+1
        return False
