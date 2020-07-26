class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S = self.StringConverter(S)
        T = self.StringConverter(T)
        S = S.replace('#', '')
        T = T.replace('#', '')
        print(S)
        print(T)
        if S==T:
            return True
        else:
            return False
        
    
    def StringConverter(self, S):
        i = 1
        while(i<len(S)):
            if i==0:
                i += 1
                continue            
            if S[i]=='#':
                S = S[:i-1] + S[i+1:]
                i -= 1
            else:
                i += 1
        return S
