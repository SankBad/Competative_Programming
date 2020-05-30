class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        num = 0
        i = 0
        if len(flowerbed)==1:
            if flowerbed[0]==1:
                return 0>=n
            else:
                return 1>=n
        while(i<len(flowerbed)):
            if i==0:
                if ((flowerbed[i]==0) and flowerbed[i+1]==0):
                    num = num + 1
                    i = i+2
                else:
                    i = i+1
            elif i==len(flowerbed)-1:
                if ((flowerbed[i]==0) and flowerbed[i-1]==0):
                    num = num + 1
                    i = i+2 
                else:
                    i = i+1
            elif ((flowerbed[i]==0) and (flowerbed[i-1]==0) and flowerbed[i+1]==0):
                num = num + 1
                i = i+2
            else:
                i=i+1
        return num>=n
            
                
                
                
            
        
