class Solution(object):
    def __init__(self):
        distance = []
        len1 = 0
        len2 = 0
        word_1 = ""
        word_2 = ""
    
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        
        Successful
        
        Faster than 98 
        Less memory than 90
        """
        self.len1 = len(word1)
        self.len2 = len(word2)
        self.word_1 = word1
        self.word_2 = word2
        self.distance = [[None] * (self.len2+1) for _ in range(self.len1+1)]
        return self.dp(self.len1, self.len2)
    
    def dp(self, x, y):
            if self.distance[x][y] is None:
                if x == 0:
                    self.distance[x][y] = y # boundary
                elif y == 0:
                    self.distance[x][y] = x # boundary
                elif self.word_1[x-1] == self.word_2[y-1]:
                    self.distance[x][y] = self.dp(x-1, y-1)
                else:
                    self.distance[x][y] = min(self.dp(x-1, y), self.dp(x, y-1), self.dp(x-1, y-1)) + 1

            return self.distance[x][y]