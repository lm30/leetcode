class Solution(object):
    def __init__(self):
        self.graph = [[]]
        self.group = []
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """     
        n = len(graph)
        self.graph = graph
        self.group = n * [-1]
        for i in range(n):
            if self.group[i] == -1:
                self.group[i] = 0
                if not self.bipart_helper(i):
                    return False
        return True

    def bipart_helper(self, i):
        for j in self.graph[i]:
            if self.group[j] != -1:
                if self.group[j] == self.group[i]:
                    return False
            else:
                self.group[j] = 1 - self.group[i]
                if not self.bipart_helper(j):
                    return False
        return True