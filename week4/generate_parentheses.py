class Solution(object):
    def __init__(self):
        self.res = []
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
            return self.res
        oc = n
        cc = n
        self.gen_helper(oc, cc, "")
        return self.res
    
    def gen_helper(self, oc, cc, prefix):
        if oc == 0 and cc == 0:
            self.res.append(prefix)
            return
        if(oc >= 1):
            self.gen_helper(oc-1, cc, prefix + "(")
        if(cc > oc and cc >= 1):
            self.gen_helper(oc, cc-1, prefix + ")")