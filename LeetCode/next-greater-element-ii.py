class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        output = [-1]*len(nums)
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(len(nums)-1):
                index = j+1+i
                if index<len(nums):
                    if curr<nums[index]:
                        output[i] = nums[index]
                        break
                else:
                    index = index-len(nums)
                    if curr<nums[index]:
                        output[i] = nums[index]
                        break
                output[i] = -1
        return output
