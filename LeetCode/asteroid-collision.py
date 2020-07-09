class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids)==0:
            return asteroids
        elif max(asteroids)<0:
            return asteroids
        elif min(asteroids)>0:
            return asteroids
        
        signmatch = True
        i = 0
        while(signmatch):
            if i==len(asteroids)-1:
                return asteroids
            prevsign = asteroids[i]
            currsign = asteroids[i+1]
            samesign = prevsign*currsign
            
            if samesign>0:
                i = i+1
            elif (samesign<0) and (asteroids[i+1]>asteroids[i]):
                i = i+1
            else:
                signmatch = False
        
        if abs(asteroids[i])==abs(asteroids[i+1]):
            del asteroids[i]
            del asteroids[i]
        elif abs(asteroids[i])>abs(asteroids[i+1]):
            del asteroids[i+1]
        else:
            del asteroids[i]
        self.asteroidCollision(asteroids)
        
        return asteroids
