class Solution:
    def isRobotBounded(self, instructions):
        dx, dy, x, y = 0, 1, 0, 0
        for l in 4*instructions:
            if l == "G": 
                x, y = x+dx, y+dy
            elif l == "L":
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx
                
        return (x,y) == (0,0)
