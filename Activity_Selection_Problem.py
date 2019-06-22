# The problem can be found at https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/
"""The following implementation assumes that the activities 
are already sorted according to their finish time"""
def printMaxActivities(s,f):
    print("Activities selected are:")
    Activity = 1
    print('0',)
    for i in range(len(s)-1):
        if f[i] < s[i+1]:
            print(i+1,)
            Activity = Activity+1
        else:
            f[i+1]=f[i]
            
# Driver program to test above function 
s = [1 , 3 , 0 , 5 , 8 , 5] 
f = [2 , 4 , 6 , 7 , 9 , 9] 
printMaxActivities(s , f) 
