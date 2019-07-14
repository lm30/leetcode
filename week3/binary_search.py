class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        Successful
        O logN
        
        62% faster
        23% less
        """
        low = 0
        high = len(nums) -1
        
        while low <= high: # while don't go past the range for list
            mid = (low + high) / 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return -1