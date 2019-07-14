class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Successful
         faster 24%
         Less mem 93%
        """
        s_nums = sorted(nums)
        res = 0
        for i in range(int(len(nums)/2)): 
            # min of every group, when sorted, is every other number
            res += s_nums[2*i]
        return res