class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
		    return [0]
        else:
            res = self.grayCode(n-1)
            temp = []
            for i in res[::-1]: # from R to L
                temp.append(i + (2 ** (n - 1))) # bin math
            res.extend(temp) # add all that appended in temp to res
            return res