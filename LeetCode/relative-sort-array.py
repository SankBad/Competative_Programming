class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        outputarr = []
        for i in arr2:
            val = arr1.count(i)
            outputarr += [i]*val
        notav = []
        for i in arr1:
            if i not in arr2:
                notav.append(i)
        notav.sort()
        return outputarr+notav
