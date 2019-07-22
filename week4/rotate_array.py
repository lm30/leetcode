from collections import deque
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        que = deque(nums)
        k = k % len(nums)
        i = 0
        while i < k: # fixed such that only one while and no for loops
            que.appendleft(que.pop())
            i += 1
        nums[:] = list(que) # array slice for every ele in array, del all and replace