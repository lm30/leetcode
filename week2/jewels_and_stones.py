class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        
        O(N)
        
        Faster than 73% submissinos
        Less memory than 72% submissions
        """
        stones = {}
        for c in S:
            if stones.get(c) == None:
                stones[c] = 1
            else:
                stones[c] += 1
        
        total = 0
        for ch in J:
            if stones.get(ch) != None:
                total += stones[ch]
        return total