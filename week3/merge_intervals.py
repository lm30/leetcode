class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort()
        n = len(intervals)
        s = intervals[0][0]
        t = intervals[0][0]
        
        res = []
        i = 0
        while t < intervals[n-1][1]:
            if i < n and t >= intervals[i][0]:
                while i < n and t >= intervals[i][0]:
                    if t < intervals[i][1]:
                        t = intervals[i][1]
                    i+=1
            else:
                res.append([s,t])
                s = intervals[i][0]
                t = intervals[i][0]
        res.append([s,t])
        return res