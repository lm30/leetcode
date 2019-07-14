class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        else:
            s1 = self.robline(nums[0:len(nums) - 1], 0, {})
            s2 = self.robline(nums[1:], 0, {})
            return max(s1, s2)
    
    def robline(self, nums, i, mem):
        if i == len(nums) - 1: # if i = 0, only 1 house, return house
            return nums[i]
        if i == len(nums) - 2: # if only 2 houses
            return max(nums[i], nums[i + 1])
        else:
            s1 = None
            s2 = None
            if i + 2 in mem:
                s1 = nums[i] + mem[i + 2]
            else:
                mem2 = self.robline(nums, i + 2, mem)
                s1 = nums[i] + mem2
                mem[i + 2] = mem2

            if i < len(nums) - 3: # if more than 3
                if i + 3 in mem:
                    s2 =  nums[i + 1] + mem[i + 3]
                else:
                    mem2 = self.robline(nums, i + 3, mem)
                    s2 = nums[i + 1] + mem2
                    mem[i + 3] = mem2
            else:
                s2 = nums[i + 1]

            return max(s1, s2)
        