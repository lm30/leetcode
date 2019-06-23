class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int

        Successful

        Faster than 98% submissions
        Less memory than 72% submissions
        """
        
        bin_n = bin(N)[2:]
        
        dist = 0
        first_one = -1
        for i in range(len(bin_n)):
            if(bin_n[i] == '1'):
                if first_one == -1:
                    first_one = i
                else:
                    if dist < i - first_one:
                        dist = i - first_one
                    first_one = i
        return dist