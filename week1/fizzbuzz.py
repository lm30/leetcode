class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]

        Successful

        Faster than 95% of submissions
        Used less memory than 85% of submissions
        """
        output = []
        for elem in range(1, n + 1):
            if(elem >= 15 and elem % 15 == 0):
                output.append("FizzBuzz")
            elif(elem >= 5 and elem % 5 == 0):
                output.append("Buzz")
            elif(elem >= 3 and elem % 3 == 0):
                output.append("Fizz")
            else:
                output.append(str(elem))
        return output