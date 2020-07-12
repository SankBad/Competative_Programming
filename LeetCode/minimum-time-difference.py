class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        for i in range(len(timePoints)):
            currM = self.ConvertMin(timePoints[i])
            timePoints[i] = currM
        
        timePoints.sort()
        
        diffT = []
        
        timePointsN = [1440 - x for x in timePoints]
        
        for j in range(len(timePoints)-1):
            diffT.append(timePoints[j+1] - timePoints[j])
            
        diffT.append(abs(1440 - timePoints[len(timePoints)-1] + timePoints[0]))
            
        return min(diffT)
            
        
    
    def ConvertMin(self, TimeH):
        TimeM = 0
        H, M = TimeH.split(':')
        TimeM = int(H)*60
        TimeM += int(M)
        return TimeM
