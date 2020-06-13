class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        q = len(nums)-1
        count = 0
        for i in nums:
            if i == 1:
                count += 1
        print(count)
        while(q-p != count-1):
            print('-----------------------')
            print(p)
            print(q)
            #print(nums[p])
            if nums[p]==0:
                #print('a')
                p = p+1
            elif nums[p]==1:
                #print('b')
                continue
            else:
               # print('c')
                temp = nums[q]
                nums[q] = 2
                nums[p] = temp
                q = q -1
                
                
                
        
