class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [nums]
        for i in xrange(1, len(nums)): # go through the nums
            num_len = len(res)
            for k in xrange(num_len):
                for j in xrange(i):
                    res.append(res[k][:]) # apend res[k] and all elems in the next col
                    temp = res[-1][i] # switch the numbers
                    res[-1][i] = res[-1][j]
                    res[-1][j] = temp
        return res