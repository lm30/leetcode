class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        sum = 0
        for item in ops:
            if item == "C": # clears 
                sum -= stack.pop()
            elif item == "D": # doubles
                sum += stack[-1] * 2
                stack.append(stack[-1] * 2)
            elif item == "+":
                sum += stack[-1] + stack[-2]
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(item))
                sum += int(item)
        return sum