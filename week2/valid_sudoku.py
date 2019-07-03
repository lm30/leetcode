class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        
        Successful
        
        on
        
        Faster than 99% submissions
        Less memory than 81% submissions
        """
        
        seen = set()
        for i in xrange(9):
            for j in xrange(9):
                num=board[i][j]
                if num!='.':
                    if (i, num) in seen:
                        return False
                    elif (num, j) in seen:
                        return False
                    elif (i//3, j//3, num) in seen:
                        return False
                    else:
                        seen.add((i, num))
                        seen.add((num, j))
                        seen.add((i//3, j//3, num))
        return True