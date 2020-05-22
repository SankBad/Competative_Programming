class Solution:
    climbs = {}
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        if n-1 not in self.climbs:
            self.climbs[n-1] = self.climbStairs(n-1)
        if n-2 not in self.climbs:
            self.climbs[n-2] = self.climbStairs(n-2)
        return self.climbs[n-1]+self.climbs[n-2]
