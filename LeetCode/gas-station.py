class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:        
        if sum(gas)-sum(cost)<0:
            return -1
        totalval = gas[0]
        curr = 0
        for i in range(len(gas)):
            totalval = totalval - cost[i] + gas[i+1]
