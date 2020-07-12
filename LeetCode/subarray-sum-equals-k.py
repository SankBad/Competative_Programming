class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currsum = 0
        myDict = {}
        myDict[0] = 1
        totnum = 0
        for i in nums:
            currsum = i + currsum
            if currsum-k in myDict:
                totnum = totnum + myDict[currsum-k] 
            
            if currsum in myDict:
                myDict[currsum] += 1
            else:
                myDict[currsum] = 1
                
        return totnum
