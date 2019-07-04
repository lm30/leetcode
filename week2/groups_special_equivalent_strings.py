class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res = dict()
        for i in A:
            if len(i) >= 2:
                key = (tuple(sorted(i[::2])), tuple(sorted(i[1::2])))
                if key not in res:
                    res[key] = 1
                else:
                    res[key] += 1
            else:
                if i not in res:
                    res[i] = 1
                else:
                    res[i] += 1
                    
        return len(res) 