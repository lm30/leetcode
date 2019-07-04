from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        
        Successful
        
        Faster than 68% submissions
        Less memory than 35% submissions
        """
        cs = Counter(s)
        
        res_list = []
        for i in cs.most_common(len(cs)): # parse through list by most common occurance
            res_list.append(i[0] * i[1]) 
        return ''.join(res_list) # convert list to string