class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        copy_arr = [i for i in range(1, len(nums)+1)]
        for i in range(len(nums)):
            j = nums[i]
            copy_arr[j-1] = -1
        output = []
        for i in range(len(nums)):
            if copy_arr[i] != -1:
                output.append(copy_arr[i])
        return output
