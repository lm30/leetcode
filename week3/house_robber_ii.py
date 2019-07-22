class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        else:
            temp1 = self.roblineone(nums[:-1])
            temp2 = self.roblineone(nums[1:])
            if temp1 > temp2:
                return temp1
            else:
                return temp2
        
    
    def roblineone(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0:2])
        for i in xrange(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        return dp[-1]