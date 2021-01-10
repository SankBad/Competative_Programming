class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        my_dict = {}
        for i in points:
            my_dict[tuple(i)] = i[0]**2 + i[1]**2
        my_arr = [a for a, b in sorted(my_dict.items(), key = lambda x: x[1])]
        return my_arr[:K]
