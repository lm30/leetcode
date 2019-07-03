class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        
        Successful
        
        on
        
        Faster than 87% submissions
        Less memory than 97 % submissions
        """
        letter_map = {} # s : t
        
        # assuming s and t have same length
        length = len(s)
        for i in xrange(length):
            # map s to t
            # if key exists already to a different letter, return false
            if s[i] in letter_map: 
                if letter_map[s[i]] != t[i]:
                    return False
            elif t[i] in letter_map.values(): 
                # if key isn't in the letter map, check if t already exists in the values
                return False
            letter_map[s[i]] = t[i]
        return True