class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        
        SUccessful
        ON
        96 % faster
        73% less
        """
        letter_dict = {}
        size = len(S)
        for i in range(size):
            letter_dict[S[i]] = i # mapping index to letter
        res = []
        char = ""
        pos = -1
        count = 0
        for i in range(size):
            count += 1
            if char != S[i] and letter_dict[S[i]] > pos:
                ch = S[i] 
                pos = letter_dict[S[i]]
            if i == pos:
                res.append(count)
                char = "" 
                pos = -1 
                count = 0
        return res