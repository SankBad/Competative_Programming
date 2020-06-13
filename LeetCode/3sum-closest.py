class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closet = float("inf")
        currsum = 0
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while(j<k):
                if abs(nums[i]+nums[j]+nums[k]-target)<closet:
                    closet = abs(nums[i]+nums[j]+nums[k]-target)
                    currsum = nums[i]+nums[j]+nums[k]
                if abs(nums[i]+nums[j+1]+nums[k]-target)<abs(nums[i]+nums[j]+nums[k-1]-target):
                    j =  j +1
                else:
                    k = k-1
        return currsum
