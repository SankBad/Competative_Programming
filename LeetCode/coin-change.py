class Solution:
    def __init__(self):
        self.MyDict = {}
        
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        calc = self.FindCoins(coins,amount)
        if calc>0:
            print(self.MyDict)
            return self.FindCoins(coins,amount)
        else:
            return -1
                
    def FindCoins(self, coins, amount):
        if amount == 0:
            return 0
        if amount<0:
            return -1
        minval = float('inf')
        for i in coins:
            if amount not in self.MyDict:
                val = self.FindCoins(coins, amount-i)
                if val>=0:
                    minval = min(val,minval)
        if minval!=float('inf'):
            self.MyDict[amount] = minval
            return self.MyDict[amount]
        else:
            return -1
            
