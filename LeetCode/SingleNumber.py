class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        MyDict = {}
        for i in nums:
            if i in MyDict.keys():
                 MyDict[i] = 2
            else:
                MyDict[i] = 1
        for i, j in MyDict.items():
            if j==1:
                return i
