class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        
        Faster than 85% submissions
        Less memory than 9% submissions
        
        Quicksort, and eliminating the need for the odd_list and even_list doesn't affect memory usage according to leetcode
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
