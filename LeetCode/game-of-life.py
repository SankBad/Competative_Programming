class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        
        next_board = [[0 for x in range(cols)] for y in range(rows)]
                
        for i in range(rows):
            for j in range(cols):
                mysum = self.CheckCell(board, i, j)
                if board[i][j]==1:
                    if mysum==2 or mysum==3:
                        next_board[i][j] = 1
                    else:
                        next_board[i][j] = 0
                else:
                    if mysum==3:
                        next_board[i][j] = 1
                    else:
                        next_board[i][j] = 0
                        
        for i in range(rows):
            for j in range(cols):
                board[i][j] = next_board[i][j]
                        
         
    def CheckCell(self, board, i, j):
        c = 0
        if i>0:
            c += board[i-1][j]
        if j>0:
            c += board[i][j-1]
        if i<len(board)-1:
            c+= board[i+1][j]
        if j<len(board[0])-1:
            c += board[i][j+1]
        if i>0 and j>0:
            c += board[i-1][j-1]
        if i>0 and j < len(board[0])-1:
            c += board[i-1][j+1]
        if i<len(board)-1 and j>0:
            c += board[i+1][j-1]
        if i<len(board)-1 and j<len(board[0])-1:
            c += board[i+1][j+1]
        
        return c
        
