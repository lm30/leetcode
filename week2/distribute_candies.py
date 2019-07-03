class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        
        Successful
        
        o1
        
        Faster than 97% submissions
        Less memory than 75% submissions
        """
        total_candies = len(candies)
        types = len(set(candies))
        
        if total_candies / 2 >= types:
            return types
        
        elif total_candies / 2 < types:
            return total_candies / 2  