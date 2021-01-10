class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_occur = {}
        for i in range(len(S)):
            last_occur[S[i]] = i
        
        ans = []
        
        j = 0
        max_occur = 0
        for i in range(len(S)):
            j = j+1
            curr_occur = last_occur[S[i]]
            if curr_occur>max_occur:
                max_occur = curr_occur
                
            if max_occur == i:
                ans.append(j)
                j = 0
                curr_occur = 0
                max_occur = 0
                
        return ans
