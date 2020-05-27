class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l = 1
        r = max(piles)
        while(l<r):
            mid = l + int((r-l)/2)
            reqt = self.FindTime(piles,mid)
            if reqt<=H:
                r=mid
            else:
                l=mid+1
        return l
            
    def FindTime(self, piles,t):
        reqt = 0
        for i in piles:
            reqt = reqt + int(i/ t) + (i% t > 0)
        return reqt
            
            
        
