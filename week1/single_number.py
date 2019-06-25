class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Successful

        Faster than 6% submissions
        Less memory than 68% submissions
        
        When using hashes, faster than 72% submissions
        Less memory than 23% submissions
        """
#         unique_list = []
#         for num in nums:
#             if num not in unique_list:
#                 unique_list.append(num)
#             else:
#                 unique_list.remove(num)
#         return unique_list[0]

        unique_h = {}
        for num in nums:
            if unique_h.pop(num, 'not_found') == 'not_found': # for default keyerror raised if key not found
                unique_h[num] = 1
        return unique_h.popitem()[0]
