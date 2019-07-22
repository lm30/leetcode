class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        
        SUccessful
        O(N)
        """
        if len(s) == 0:
            return True
        if len(s) % 2 == 1: # if odd number than will never be balanced
            return False
        stack = []
        
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            if stack:
                if ch == ")" and stack[-1] == "(": # if matches, remove the opening
                    stack.pop()
                elif ch == "}" and stack[-1] == "{":
                    stack.pop()
                elif ch == "]" and stack[-1] == "[":
                    stack.pop()
        return stack == []