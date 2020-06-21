class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        myDict = {}
        for i in range(len(nums2)-1, -1, -1):
            myDict[nums2[i]] = -1
            while(len(stack)!=0):
                if stack[-1]>nums2[i]:
                    myDict[nums2[i]]=stack[-1]
                    break
                else:
                    stack.pop()
            stack.append(nums2[i])
        output = []
        for i in nums1:
            output.append(myDict[i])
        return output
