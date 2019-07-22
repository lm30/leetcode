class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mysum = sum(nums)
        if mysum % 2: # if odd number
            return False
        if len(nums) < 2: # if 1 or 0 elems
            return False
        nums.sort() # sort from smallest to largest
        return self.part_helper(nums, mysum/2)
    
    def part_helper(self, nums, target):
        if not target: 
            return True
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: # if they're equal, next number
                continue
            if target >= nums[i]: 
                # if target unfulfilled, 
                # recurse until find fulfillment with remaining nums in list
                if self.part_helper(nums[i+1:], target - nums[i]):  
                    return True
        return False