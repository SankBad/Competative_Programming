class Solution:
    memo = {}
    def fib(self, N: int) -> int:
        if N<2:
            return N
        if N-1 not in self.memo:
            self.memo[N-1]= self.fib(N-1)
        if N-2 not in self.memo:
            self.memo[N-2]= self.fib(N-2)
        
        return self.memo[N-1] + self.memo[N-2]
        
