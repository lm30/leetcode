class Solution(object):
    
    def try_happy(self, n):
        sum = 0
        for c in list(str(n)):
            sum += int(c) * int(c)
        return sum
    
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        
        Successful
        
        Faster than 87% 
        less memory than 79%
        """
        seen = set()
        
        while n != 1 and n not in seen:
            # check happiness of number then send it to seen
            seen.add(n)
            n = self.try_happy(n)
        return n == 1