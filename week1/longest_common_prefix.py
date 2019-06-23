class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str

        Faster than 87% submissions
        Less memory than 66% submissions
        """
        if len(strs) == 1:
            return strs[0]
        if len(strs) == 0:
            return ""
        
        prefix = ""
        min_len = sys.maxint
        for i in range(len(strs)): # find length of smallest string in strs
            if min_len > len(strs[i]):
                min_len = len(strs[i])

        for j in range(min_len):
            ith_letter = [string[j] for string in strs]
            if max(ith_letter) != min(ith_letter):
                return prefix
            else:
                prefix = prefix + ith_letter[0]
        return prefix