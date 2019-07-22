class Solution(object):        
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        target, remainder = divmod(sum(nums), k)
        if remainder != 0: # if the sum can't be divided by 4, return
            return False

        nums.sort()
        nums = nums[::-1] # sort and reverse
        n = k # need b/c will change the val later
        s = 0
        while s < len(nums):
            if nums[s] < target:
                break
            elif nums[s] > target: # if any of the nums greater, can't make eq subsets
                return False
            else:
                n -= 1
            s += 1
        bins = [target] * n 
        return self.find_subs(nums, s, bins, target * n)
    
    def find_subs(self, nums, s, bins, remain):
            if remain == 0:
                return True
            for i in range(len(bins)):
                if nums[s] <= bins[i]:
                    bins[i] -= nums[s]
                    if 0 < bins[i] < nums[-1]:
                        bins[i] += nums[s]
                        continue
                    if self.find_subs(nums, s+1, bins, remain-nums[s]):
                        return True
                    bins[i] += nums[s]
            return False
        