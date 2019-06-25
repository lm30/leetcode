class Solution(object):
    def __init__(self):
        self.count = 0
    
    def find(self, indexes, i):
        if indexes[i] != i:
            indexes[i] = self.find(indexes, indexes[i])
        return indexes[i]

    def union(self, indexes, i, j):
        ivert = self.find(indexes, i)
        jvert = self.find(indexes, j)
        
        if ivert == jvert: # cycle detected
            return
        indexes[ivert] = jvert   
        self.count -= 1 # remove possible islands from count
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        Successful

        Faster than 85% submissions
        Less memory than 81% submissions
        """
        if grid==[]: return 0
        rows = len(grid)
        cols = len(grid[0])
        
        idxs = []
        for i in range(rows): # count all 1's or max possible number islands
            for j in range(cols):
                if grid[i][j] == "1":
                    self.count += 1
        for i in range(rows * cols):
            idxs.append(i)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '0': 
                    continue
                curr = i * cols + j 
                if j < cols-1: 
                    if grid[i][j+1] == '1':
                        self.union(idxs, curr, curr + 1)
                if i < rows-1:
                    if grid[i+1][j] == '1':
                        self.union(idxs, curr, curr + cols)
        return self.count