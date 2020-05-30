class Solution:
    def __init__(self):
        self.myDict = {}
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        totalcost = self.findMinCost(cost,0)
        return totalcost
    
    def findMinCost(self, cost, i):
        if i>=len(cost)-1:
            return 0
        if i+1 not in self.myDict:
            self.myDict[i+1] = self.findMinCost(cost,i+1)
        if i+2 not in self.myDict:
            self.myDict[i+2] = self.findMinCost(cost,i+2)            
            
        return min(cost[i]+self.myDict[i+1],cost[i+1]+self.myDict[i+2])
        
        
