# The problem can be found at https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/
"""The following implementation works without sorted array"""


def printMaxActivities(s,f):
    arr = sorted(range(len(f)), key=lambda k: f[k])
    f.sort()
    temp = s
    Activity = 1
    print('0')
    for i in range(len(s)):
        s[i] = temp[arr[i]]
    for i in range(len(s)-1):
        if f[i] < s[i+1]:
            print(i+1,)
            Activity = Activity+1
        else:
            f[i+1]=f[i]



# Driver program to test above function 
s = [5 , 1 , 3 , 0 , 5 , 8] 
f = [9 , 2 , 4 , 6 , 7 , 9] 
printMaxActivities(s , f) 
