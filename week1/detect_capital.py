class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool

        Successful
        Faster than 96% submissions
        Less memory than 29% submissions
        """
        cap_count = 0
        first_letter = False
        for i in range(len(word)):
            if(word[i].isupper()): # counts how many upper case to compare later
                cap_count += 1
                if(i == 0): # is the first letter capitalized
                    first_letter = True
        
        if(cap_count == 0):
            return True
        else:
            if(cap_count == 1 and first_letter == True):
                return True
            elif(cap_count == len(word)):
                return True
            else:
                return False