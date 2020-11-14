class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        l_dir = {'N':'W','W':'S','S':'E','E':'N'}
        r_dir = {'N':'E','E':'S','S':'W','W':'N'}
        my_dict = {'N':(1,0), 'S':(-1,0), 'E':(0,1), 'W':(0,-1)}
        my_dir = 'N'
        my_loc = (0,0)
        for i in instructions:
            if i=='G':
                my_dir = my_dir
                my_loc = (my_loc[0] + my_dict[my_dir][0], my_loc[1] + my_dict[my_dir][1])
            elif i=='L':
                my_dir = l_dir[my_dir]
            elif i=='R':
                my_dir = r_dir[my_dir]
        if my_loc==(0,0) or my_dir !='N':
            return True
        else:
            return False
