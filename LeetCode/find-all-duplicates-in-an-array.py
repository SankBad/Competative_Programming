class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        l = 0
        duplicate = []
        while(l!=len(nums)):
            currelem = nums[l]
            if currelem==-1:
                l += 1
            else:
                temp = nums[currelem-1]
                if temp==-1:
                    duplicate.append(currelem)
                    l += 1
                else:
                    nums[l]=temp
                    nums[currelem-1]=-1
        return set(duplicate)
