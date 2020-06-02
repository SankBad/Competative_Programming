class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []
        nums1.sort()
        for j in nums2:
            l = 0
            r = len(nums1)-1
            while(l<=r):
                mid = l + (r-l)//2
                print(nums1[mid])
                if nums1[mid]==j:
                    intersection.append(j)
                    break
                elif nums1[mid]<j:
                    l = mid+1
                else:
                    r = mid-1
        print(intersection)
        return list(set(intersection))
                    
        
