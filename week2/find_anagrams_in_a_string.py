from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        
        Successful
        
        Faster than 36%
        Less memory than 50%
        """
        ret_list = []
        lim = len(p)
        cp = Counter(p)
        cs = Counter(s[:lim -1]) # limit visiblity to length of p
        
        for i in range(lim -1,len(s)):
            c = s[i]
            cs[c] += 1 # add to the counter 
            old_char_idx = i - lim + 1 # get oldest character visible by counter cs
            old_char = s[old_char_idx]
            if cs == cp:
                ret_list.append(old_char_idx)
            cs[old_char] -= 1 # remove oldest from cs counter to limit visibility
            if cs[old_char] == 0:
                del cs[old_char]
        return ret_list