class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        
        Successful
        O(N)
        
        Faster than 86% 
        Less memory than 18%
        """
        drawer = {5: 0, 10: 0}
        for customer in bills:
            if customer % 5 != 0:
                return False
            elif customer == 5:
                drawer[customer] += 1
            elif customer == 10:
                if drawer[5] > 0:
                    drawer[5] -= 1
                    drawer[10] += 1
                else: return False
            elif customer == 20:
                if drawer[10] > 0 and drawer[5] > 0:
                    drawer[10] -= 1
                    drawer[5] -= 1
                elif drawer[5] > 2:
                    drawer[5] -= 3
                else: return False
        return True