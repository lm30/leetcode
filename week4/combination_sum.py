class Solution(object):
    def __init__(self):
        self.res = []
        self.target = 0
        self.candidates = []
        
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.target = target
        self.candidates = candidates
        self.backtrack(0, 0, [])
        return self.res
    
    def backtrack(self, idx, cur, ans):
        if cur == self.target:
            self.res.append(ans)
            return
        if cur > self.target:
            return
        i = idx
        while i < len(self.candidates):
            self.backtrack(i, cur + self.candidates[i], ans + [self.candidates[i]])
            while i + 1 < len(self.candidates) and self.candidates[i + 1] == self.candidates[i]:
                i += 1
            i += 1