class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if length==0:
            return -1
        l = 0
        r = length-1
        if nums[l]==target:
            return l
        elif nums[r]==target:
            return r
        while(l<=r):
            mid = l + (r-l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[l]:
                if nums[mid]>target and nums[l]<=target:
                    r=mid-1
                else:
                    l = mid+1
            else:
                if nums[mid]<target and nums[r]>=target:
                    l=mid+1
                else:
                    r = mid-1
        return -1
