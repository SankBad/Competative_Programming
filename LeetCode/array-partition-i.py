class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        totalsum = 0
        for i in range(0,len(nums)-1,2):
            totalsum = totalsum + nums[i]
        
        return totalsum
        
