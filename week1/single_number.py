class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Successful

        Faster than 6% submissions
        Less memory than 68% submissions
        """
        unique_list = []
        for num in nums:
            if num not in unique_list:
                unique_list.append(num)
            else:
                unique_list.remove(num)
        return unique_list[0]