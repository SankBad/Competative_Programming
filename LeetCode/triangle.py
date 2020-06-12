class Solution:
    def __init__(self):
        self.MyDict = {}
        
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.minRoute(triangle,0,0)
    
    def minRoute(self,triangle,ro,i):
        if ro==len(triangle):
            return 0
        First = (ro+1)*(ro+2)/2 + i
        Second = (((ro+1)*(ro+2)/2) + i+1)
        
        if First not in self.MyDict:
            self.MyDict[First] = self.minRoute(triangle,ro+1,i)
            
        if Second not in self.MyDict:
            self.MyDict[Second] = self.minRoute(triangle,ro+1,i+1)
                        
        
        return  min(triangle[ro][i]+self.MyDict[First], triangle[ro][i]+self.MyDict[Second])
        
