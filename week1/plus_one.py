class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        Successful

        Faster than 82% submissions
        Used less than 63% submissions
        """
        dig_string = ""
        for elem in digits:
            dig_string += str(elem)
        dig_string = str(int(dig_string) + 1)
        
        return list(map(int, str(dig_string)))