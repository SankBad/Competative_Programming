class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        output = []
        for i in range(len(T)-1):
            for j in range(i+1,len(T)):
                if T[j]>T[i]:
                    output.append(j-i)
                    break
                if j==len(T)-1:
                    output.append(0)
        output.append(0)
        return output
