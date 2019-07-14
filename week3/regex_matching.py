class Solution(object):
    def __init__(self):
        self.mem = {}
    
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        
        Successful
        
        Faster than 99%
        Less memory than 15%
        """
        if (s, p) in self.mem:
            return self.mem[(s, p)]
        if not p:
            return s == ''
        
        res = False
        if len(p) > 1 and p[1] == '*':
            res = self.isMatch(s, p[2:]) or (s != '' and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p))
        else:
            res = s != '' and (p[0] == '.' or s[0] == p[0]) and self.isMatch(s[1:], p[1:])
        self.mem[(s, p)] = res
        return res