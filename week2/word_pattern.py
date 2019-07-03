class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        
        Successful
        
        on
        
        Faster than 94% submissions
        Less memory than 82% submissions
        """
        
        word_map = {} # maps letter : word
        
        letter_len = len(pattern)
        word_list = str.split(" ")
        sent_len = len(word_list)
        
        if letter_len != sent_len:
            return False
        
        for i in xrange(letter_len):
            if pattern[i] in word_map: 
                if word_map[pattern[i]] != word_list[i]:
                    return False
            elif word_list[i] in word_map.values(): 
                # if key isn't in the word map, check if word already exists in the values
                return False
            word_map[pattern[i]] = word_list[i]
        return True