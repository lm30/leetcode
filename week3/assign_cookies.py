class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        
        Successful
        
        Faster than 60 % 
        Less memory than 91%
        """
        s.sort() # sort s and g so the lists are both going in inc order
        g.sort()
        res = 0
        while s and g:
            if s[-1] < g[-1]: 
                # if the cookie size (last ele of s) is less than satisfctory, 
                # rm child (by their greed factor)
                g.pop()
            else:
                res += 1
                s.pop() # child and cookie were satisfied
                g.pop()
        return res