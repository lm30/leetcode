class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        Successful
        
        Faster than 63
        Less memory than 83
        """
        return self.recurse(x, n)
    
    def recurse(self, a, b):
        if b < 0:
            return self.recurse(1/a, -b)
        if b == 0:
            return 1 
        ans = self.recurse(a * a, b // 2)
        return ans if b % 2 == 0 else ans * a
