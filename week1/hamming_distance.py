class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int

        Successful

        Faster than 23% submissions
        Less memory than 85% submissions
        """
        
        xbin = bin(x)[2:]
        ybin = bin(y)[2:]
        print xbin
        print ybin
        if len(xbin) > len(ybin): # reverse string because read binary right to left
            return self.find_ham_distance(xbin[::-1], ybin[::-1]) 
        else: #pass through function where larger number goes first
            return self.find_ham_distance(ybin[::-1], xbin[::-1])
    
    def find_ham_distance(self, large_bin, small_bin):
        count = 0
        for i in range(len(large_bin)):
            compare_bit = '0'
            if(i < len(small_bin)):
                compare_bit = small_bin[i]
            
            if(int(large_bin[i]) != int(compare_bit)):
                count += 1
        return count