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
    
        len1 = len(word1)+1
        len2 = len(word2)+1
        res = [[0 for _ in xrange(len2)] for _ in xrange(len1)]
        for i in xrange(len1):
            res[i][0] = i
        for j in xrange(len2):
            res[0][j] = j
        for i in xrange(1, len1):
            for j in xrange(1, len2):
                res[i][j] = min(res[i-1][j]+1, res[i][j-1]+1, res[i-1][j-1]+(word1[i-1]!=word2[j-1]))
        return res[-1][-1]