from collections import Counter
import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        
        Successful
        
        Faster than 92% submissions
        Less memory than 44% submissions
        """
        c_para = Counter(re.split('[^a-zA-Z]', paragraph.lower()))
        c_ban = Counter(banned)
        del c_para[''] # remove the '' left after removing the non alphanumeric characters
        for i in c_para.most_common(len(c_para)):
            if i[0] not in c_ban:
                return str(i[0])