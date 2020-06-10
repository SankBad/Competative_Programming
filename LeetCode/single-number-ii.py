class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        MyDict = {}
        for i in nums:
            if i not in MyDict.keys():
                MyDict[i] = 1
            else:
                MyDict[i] = MyDict[i]+ 1
        
        for i in MyDict:
            if MyDict[i]==1:
                return i
