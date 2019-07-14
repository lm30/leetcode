class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        
        Successful
        ON
        
        Faster than 96%
        Less memory than 20%
        """
        sort_pts = sorted(points, key = lambda x: x[1]) # sort by x
        
        prev_shot = -1000000000000000
        count = 0

        for bal in sort_pts:
            if bal[0] > prev_shot:
                prev_shot = bal[1]
                count += 1
                
        return count