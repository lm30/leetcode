class Solution(object):
    
    def __init__(self):
        self.parent = []
        self.rank = []
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        ivert = self.find(i)
        jvert = self.find(j)
        
        if ivert == jvert: # cycle detected
            return
        if self.rank[ivert] < self.rank[jvert]:
            self.parent[ivert] = jvert
        else: # need to use ranks
            if self.rank[ivert] == self.rank[jvert]:
                self.rank[ivert] += 1;
            self.parent[jvert] = ivert
        # self.parent[ivert] = jvert 
        # self.surrounded = self.surrounded[ivert] and self.surrounded[jvert]
        
    
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.

        Successful but need to redo it

        Faster than 5% submissions
        Less memory than 11% submissions
        """
        if not board: return
        rows = len(board)
        cols = len(board[0])
        
        self.parent = range(rows * cols)
        self.rank = range(rows * cols)
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'X':
                    continue
                curr = i * cols + j
                if i == 0 or j == 0 or i == rows -1 or j == cols -1: # for the edges of board
                    self.union(curr, rows * cols -1)

                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if x >= 0 and x < rows and y >= 0 and y < cols and board[x][y] == 'O':
                        self.union(curr, x*cols + y)

        for i in range(rows): # for repainting board
            for j in range(cols):
                if board[i][j] == 'O' and self.find(i * cols + j) != rows * cols -1:
                    board[i][j] = 'X'