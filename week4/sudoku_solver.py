class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.sudo_helper(board)
        
    def sudo_helper(self, board):
        x = -1
        y = -1
        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col] == '.':
                    y = col
                    x = row
                    break
            if x != -1:
                break
        if x == -1:
            return True
        
        # for that x and y
        tmp = [str(i) for i in range(1,10)] # creates string of possible sudo vals
        for col in range(0, 9): # go trhough col and row of board and rm matches 
            if board[x][col] in tmp:
                tmp.remove(board[x][col])
                
        for row in range(0, 9):
            if board[row][y] in tmp:
                tmp.remove(board[row][y])
                
        for row in range(x//3*3, x//3*3 +3): # moving by boxes
            for col in range(y//3*3, y//3*3 +3):
                if board[row][col] in tmp:
                    tmp.remove(board[row][col])
        for i in tmp:
            board[x][y] = i
            if self.sudo_helper(board):
                return True
            board[x][y] = '.'
        return False