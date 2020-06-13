class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        q = len(nums)-1
        r = 0
        count = 0
        while(r<=q):
            if nums[r]==0:
                temp = nums[p]
                nums[p] = 0
                if temp==1:
                    nums[r] = 1
                r = r+1
                p = p+1
            elif nums[r]==1:
                r = r+1
            else:
                temp = nums[q]
                nums[q] = 2
                nums[r] = temp
                q = q -1
