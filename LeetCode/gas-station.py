class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:        
        if sum(gas)-sum(cost)<0:
            return -1
        totalval = 0
        curr = 0
        for i in range(len(gas)):
            totalval = totalval + gas[i] - cost[i]
            if totalval<0:
                curr = i+1
                totalval = 0
        return curr
