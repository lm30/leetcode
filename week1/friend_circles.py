class Solution(object):
    def __init__(self):
        self.parent = []
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        ivert = self.find(i)
        jvert = self.find(j)
        
        if ivert == jvert: # cycle detected
            return
        self.parent[ivert] = jvert  
    
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int

        Successful

        Faster than 49% submissions
        Less memory than 49% submissions
        """
        if not M: return 0
        rows = len(M)
        self.parent = range(rows)
        
        for i in range(rows):
            for j in range(i, rows):
                if M[i][j] == 1: 
                    self.union(i,j)
                    
        return sum([self.find(x) == x for x in range(rows)])