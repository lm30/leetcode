class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool

        Revisit needed if want to finish bit counting solution
        
        Successful 
        
        Faster than 93% submissions
        Less memory than 18% submissions
        """
        return n & (n -1) == 0 and n != 0
        
