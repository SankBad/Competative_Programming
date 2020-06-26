class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        MyDict = dict(Counter(nums))
        MyDict = {k:v for  k, v  in (sorted(MyDict.items(), key= lambda x: x[1], reverse=True))}
        output = []
        j = 0
        for i in MyDict.keys():
            j +=1
            output.append(i)
            if j==k:
                break
        return output
