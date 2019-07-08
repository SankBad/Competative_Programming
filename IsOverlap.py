def isOverlap(Arr):
    Arr.sort()
    Overlap = False
    for i in range(len(Arr)-1):
        if Arr[i+1][0]<Arr[i][1]:
            Overlap = True
            break
    return Overlap       

List = [[1, 3], [5, 7], [2, 4], [6, 8]]
print(isOverlap(List))
List = [[1, 3], [7, 9], [4, 6], [10, 13]]
print(isOverlap(List))
