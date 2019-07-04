from collections import Counter

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        
        Successful
        
        Faster than 40% submissions
        Less memory than 22% submissions
        """
        c_nums = Counter(nums)
        dup_n = 0
        lost_n = 0
        for i in xrange(1, len(nums) + 1): # add 1 because start at 1 not 0
            if i not in c_nums: # parse through every number until find lost n
                lost_n = i
            elif c_nums[i] > 1:
                dup_n = i
        if lost_n == 0 : # if can't find lost num, and duplicate is 1, 
            # then haven't reached lost num yet, it's 2
            if dup_n == 1:
                lost_n = 2
        return [dup_n, lost_n]