class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = 0
        for i in range(len(nums)):
            if nums[length] != nums[i]:
                length = length+1
                nums[length] = nums[i]
        return length+1
