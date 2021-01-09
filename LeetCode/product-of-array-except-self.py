class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_arr = [1]
        right_arr = [1]
        for i in range(len(nums)-1):
            left_arr.append(left_arr[-1]*nums[i])
        
        right_arr = [1]
        for j in range(len(nums)-1, 0, -1):
            right_arr.append(right_arr[-1]*nums[j])
        
        right_arr.reverse()
        
        ans = []
        for i in range(len(nums)):
            ans.append(left_arr[i]*right_arr[i])
        return ans
