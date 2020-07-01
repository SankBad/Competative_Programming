class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points = sorted(points, key = self.myfunc)
        return points[:K]
    
    def myfunc(self, x):
        return x[0]**2 + x[1]**2
