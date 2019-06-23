class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Successful

        Faster than 87% submissions
        Less memory than 16.31% submissions
        """
        num_dict = {}
        
        for i in range(len(nums)):
            # if second number not in the dictionary, add first number to dict
            if target - nums[i] not in num_dict:
                num_dict[nums[i]] = i
            else: # if found second number in the dict to first one, return the pair
                return [num_dict[target - nums[i]], i]