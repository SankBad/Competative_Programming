# Solution to https://www.geeksforgeeks.org/greedy-algorithm-egyptian-fraction/
import math
def EgyptianFraction(n,d):
    x = math.ceil(d/n)
    print(" 1/{0} +" .format(x), end = " ") 
    y=n/d-1/x
    if y==0:
        return
    EgyptianFraction(n*x-d,d*x)    
    
    
EgyptianFraction(6, 14)
