class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        first = m-1
        second = n-1
        for i in range(m+n-1,-1,-1):
            if (first == -1):
                nums1[i]=nums2[second]
                second = second - 1
                continue
            if second==-1:
                break
            if nums1[first]<nums2[second]:
                nums1[i]=nums2[second]
                second = second - 1
            else:
                nums1[i]=nums1[first]
                first = first - 1
