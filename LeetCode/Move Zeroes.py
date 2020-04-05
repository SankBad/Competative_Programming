class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = len(nums)
        for i in nums:
            if i!=0:
                nums[l] = i
                l = l+1
        for i in range(l,r):
            nums[i] = 0
