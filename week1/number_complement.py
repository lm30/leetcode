class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int

        Successful

        Faster than 95% submissions
        Less memory than 5.36% submissions
        """
        bnumber = bin(num)[2:]
        compl = ''
        
        for bit in bnumber:
            if bit == '1':
                compl += '0'
            else:
                compl += '1'
        return int(compl, 2)