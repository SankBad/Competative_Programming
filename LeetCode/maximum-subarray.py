class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        LargestSum = sum(nums)
        currsum=LargestSum
        length = len(nums)
        l = 0
        r = length-1
        while(l<r):
            if nums[l]<nums[r]:
                currsum = currsum-nums[l]
                l=l+1
            else:
                currsum = currsum-nums[r]
                r = r-1
            if currsum>LargestSum:
                LargestSum = currsum
        return LargestSum
                
            
            
        
