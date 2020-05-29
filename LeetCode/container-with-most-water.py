class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        i = 0
        j = len(height)-1
        while(i<=j):
            height1 = min(height[i],height[j])
            currarea = height1*(j-i)
            if  (maxarea < currarea):
                maxarea=currarea
            if height1==height[i]:
                i = i+1
            else:
                j = j-1
        return maxarea
