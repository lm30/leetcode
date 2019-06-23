class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool

        Revisit needed, passes test cases but not submission
        """
        total = 0
        bin_n = bin(n)[2:]
        for elem in bin_n:
            total += int(str(elem))
        return total == 1
        