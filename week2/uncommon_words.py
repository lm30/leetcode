class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        
        Successful
        
        on
        Faster than 98% submissions
        Less memory than 31% submissions
        """
        
        usets = set(A.split(" ")).union(set(B.split(" ")))
        
        repeated_words = {}
        for word in A.split(" "):
            if word in repeated_words:
                usets.discard(word) # discard won't raise error if doesn't exist in set
            else:
                repeated_words[word] = 1
        
        for word in B.split(" "):
            if word in repeated_words:
                usets.discard(word)
            else:
                repeated_words[word] = 1
        return list(usets)