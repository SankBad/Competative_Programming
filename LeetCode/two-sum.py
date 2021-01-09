class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            if target-nums[i] not in my_dict:
                my_dict[nums[i]]=i
            else:
                return [i, my_dict[target-nums[i]]]
        return -1
