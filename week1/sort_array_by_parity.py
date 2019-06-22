class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd_list = []
        even_list = []
        for num in A:
            if(num % 2 == 1):
                # odd numbers
                odd_list.append(num)
            else:
                # even numbers
                even_list.append(num)
        return even_list + odd_list