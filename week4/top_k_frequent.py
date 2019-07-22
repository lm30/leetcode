from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        heap = []
        dic = Counter(nums)
        
        for key in dic:
            temp = (dic[key], key) # temp = (freq, value)
            if len(heap) >= k:
                # take out smallest ele in heap after adding temp
                heapq.heappushpop(heap, temp) 
            else: # add ele to heap
                heapq.heappush(heap, temp)
                
        res = []
        for i in range(len(heap)):
            res.append(heapq.heappop(heap)[1]) # put val in the result
        return res[::-1] # reversed slice