class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]

        Successful

        Faster than about 80%
        Less memory than 60% 
        """
        output = []
        for elem in range(left, right + 1):
            if(elem % 10 == 0): # skip this number because divide by zero error
                continue
            self.check_self_divide(elem, 0, len(str(elem)), output)
        return output
    
    def check_self_divide(self, elem, n, length, output):
        if(n < length):
            num = int(str(elem)[n])
            if(num != 0 and elem % num == 0):
                self.check_self_divide(elem, n+1, length, output)
            else:
                return False
        else:
            output.append(elem)
            return True