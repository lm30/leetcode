from collections import Counter

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        
        Successful
        
        Faster than 76% 
        Less memory than 57%
        """
        cs = Counter(s)
        ct = Counter(t)
        
        return list(ct - cs)[0]