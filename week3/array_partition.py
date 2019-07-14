class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s_nums = sorted(nums)
        res = 0
        for i in range(int(len(nums)/2)):
            res += s_nums[2*i]
        return res