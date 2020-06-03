class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        outputarr = []
        for j in range(left,right+1):
            if self.selfdivnum(j):
                outputarr.append(j)
            else:
                continue
        return outputarr
                
    
    def selfdivnum(self, num):
        numstr = str(num)
        for i in numstr:
            if int(i)==0:
                return False
            else:
                if num%int(i)==0:
                    continue
                else:
                    return False
        return True
            
        
