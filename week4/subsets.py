class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == None:
            return []
        elif nums == []:
            return [[]]
            
        res=[]
        
        self.sub_help(nums, [], res, 0)
        return res

    def sub_help(self, nums, temp, ret_res, i):
        if i == len(nums):
            ret_res.append(temp[:])
            return
        
        self.sub_help(nums,temp,ret_res,i+1)
        temp.append(nums[i])
        self.sub_help(nums,temp,ret_res,i+1)
        temp.remove(temp[-1])