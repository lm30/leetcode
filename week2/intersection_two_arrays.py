class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        
        Successful
        
        Faster than 95% submissions
        Less  memory than 58%% submissions
        """
        return set(nums1).intersection(set(nums2))