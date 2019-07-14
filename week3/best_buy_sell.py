class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if not prices:
            return 0
        
        buy = prices[0]
        res = 0
        for price in prices[1:]: # for every price after the first price
            if price < buy: # if price is lower than th buy, that is the new low
                buy = price
            else:
                if res < price - buy:
                    res = price - buy
        return res