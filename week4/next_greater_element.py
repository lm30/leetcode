class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        
        Successful
        
        O(N)
        """
        res = []
        stack = []
        dic = {}
        for num in nums2: # go through nums2 append them to the stack
            # if last ele of stack is less than current num, 
            # remove it from stack and greater number is stored in the dict as 
            # the val to that key
            while stack != [] and stack[-1] < num:
                dic[stack.pop()] = num
            stack.append(num)
        
        for num in nums1:
            if num in dic.keys():
                res.append(dic[num])
            else:
                res.append(-1)
        return res