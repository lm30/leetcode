class Solution(object):
    def __init__(self):
        self.k = 0
        self.n = 0
        self.res = []
    
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # edge cases
        if n <= 0:
            return []
        if k > n: # if nums expected to make combos with greater than num ofnums
            return []
        
        self.k = k
        self.n = n
        self.comb_helper(1, [])
        return self.res
    
    def comb_helper(self, pos, path):
        if len(path) == self.k:
            self.res.append(path[:]) # append entire copy path to result
            return
        if len(path) + self.n - pos + 1 < self.k:
            return
        for i in range(pos, self.n+1):
            path.append(i)
            self.comb_helper(i+1, path)
            path.pop()