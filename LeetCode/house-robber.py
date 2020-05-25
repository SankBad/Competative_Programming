class Solution:
    def __init__(self):
        self.MyDict = {}
    def rob(self, nums: List[int]) -> int:
        return self.rob_amount(nums,0)
        
    def rob_amount(self, nums,i):
        length = len(nums)
        if i+1-length>0:
            return 0
        if i+1 not in self.MyDict:
            self.MyDict[i+1] = self.rob_amount(nums,i+1)
        if i+2 not in self.MyDict:
            self.MyDict[i+2]= self.rob_amount(nums,i+2)            
        output =  max(nums[i]+self.MyDict[i+2], self.MyDict[i+1])
        return output
