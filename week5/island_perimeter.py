class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perim = 0
        # lists by rows then by cols, so 4x4 would be a 8 x 4 matrix
        grid +=  ([[row[i] for row in grid] for i in range(len(grid[0]))])
        for row in grid:
            row = [0] + row + [0] # adds 0s to front and back of list of rows 
            # s.t. can test for each elem, can see if has land to left and right of it
            for i in range(1, len(row)):
                if row[i] != row[i-1]:
                    perim += 1

        return perim