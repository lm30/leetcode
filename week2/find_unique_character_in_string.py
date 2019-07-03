from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        
        Successful
        
        on
        
        Faster than 34% submissions
        Less memory than 80% submissions
        """
        count = Counter(s)
        i = 0
        for c in s:
            if count[c] == 1:
                return i
            i+= 1
        
        return -1