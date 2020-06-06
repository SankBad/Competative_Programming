class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=1
        r = len(nums)-2
        if r==-1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[r]<nums[r+1]:
            return r+1
        while(l<=r):
            mid = l + (r-l)//2
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid]<nums[mid+1]:
                l=mid+1
            else:
                r=mid-1
