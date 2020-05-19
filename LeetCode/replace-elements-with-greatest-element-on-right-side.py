class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_val = -1
        output_arr = [0]*len(arr)
        output_arr[len(arr)-1]=max_val
        for i in range(len(arr)-2, -1, -1):
            if arr[i+1]>max_val:
                output_arr[i]=arr[i+1]
                max_val = arr[i+1]
            else:
                output_arr[i]=max_val                
        return output_arr
