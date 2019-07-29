class Solution(object):
    def __init__(self):
        self.M = []
        self.N = []
        self.word = ""
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        queue = []
        self.M = len(board)
        self.N = len(board[0])
        self.word = word
        
        for i in range(self.M):
            for j in range(self.N):
                if self.word_helper(i, j, board, 0):
                    return True

                
    def word_helper(self, i,j,b,index): # dfs
            if index == len(self.word):
                return True
            if i < 0 or j < 0 or i == self.M or j == self.N:
                return False
            if b[i][j] != self.word[index]:
                return False
            tmp = b[i][j]
            b[i][j] = '0'
            ans = self.word_helper(i-1,j,b,index+1) or self.word_helper(i+1,j,b,index+1) or self.word_helper(i,j-1,b,index+1) or self.word_helper(i,j+1,b,index+1) 
            b[i][j] = tmp
            return ans