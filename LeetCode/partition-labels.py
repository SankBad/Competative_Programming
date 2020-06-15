class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        totallen = len(S)-1
        l = 0
        outputarr = []
        while(l<=totallen):            
            start = l
            r = S.rfind(S[start])
            l = start + 1
            while(l<=r):
                rpos = S.rfind(S[l])
                if rpos<=r:
                    l += 1
                else:
                    l += 1
                    r = rpos
            val = r-start+1
            outputarr.append(r-start+1)
        return outputarr
