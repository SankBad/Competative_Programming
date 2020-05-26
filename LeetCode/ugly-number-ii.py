class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i = 1
        uglynum = [1]
        first = second = third =  0
        while(i<n+1):
            first_num = uglynum[first]*2
            second_num = uglynum[second]*3
            third_num = uglynum[third]*5
            
            min_ugly = min(first_num,second_num,third_num)
            uglynum.append(min_ugly)
            if (min_ugly==first_num):
                first = first + 1
            if (min_ugly==second_num):
                second = second + 1
            if (min_ugly==third_num):
                third = third + 1
            i = i+1
        return uglynum[n-1]
                
            
            
            
