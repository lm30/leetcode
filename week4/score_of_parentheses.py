class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        
        Successful
        O(N)
        """
        if len(S) == 0:
            return 0
        
        stack = []
        val = 0
        for i in range(len(S)):
            if S[i] == "(":
                stack.append(S[i])
            else:
                if S[i-1] == "(": # if prev ele is ( or this is a ()
                    val += 2 ** (len(stack) - 1) # computes completed section in stack so far
                    # to take into account multiple nesting, uses power of two
                stack.pop()
        return val