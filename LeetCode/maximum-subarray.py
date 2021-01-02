class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = -float('inf')
        currsum = 0
        for i in range(len(nums)):
            currsum = max(nums[i], currsum + nums[i])
            if currsum>maxsum:
                maxsum = currsum
        return maxsum
            
            
        
