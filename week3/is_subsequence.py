class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        
        Successful
        O(N)
        
        Faster than 68% 
        Less memory than 24%
        """
        idx = 0
        size = len(s)
        for i in range(len(t)):
            if size > idx and t[i] == s[idx]:
                idx += 1
        return idx == size