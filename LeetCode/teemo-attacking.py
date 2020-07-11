class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries)==0:
            return 0
        total_d = 0
        curr = timeSeries[0]
        for i in range(1, len(timeSeries)):
            curr = curr + duration
            if curr>timeSeries[i]:
                total_d = total_d + (timeSeries[i]-timeSeries[i-1])
                curr = timeSeries[i]
            else:
                total_d = total_d + duration
                curr = timeSeries[i]
        
        return total_d+duration
