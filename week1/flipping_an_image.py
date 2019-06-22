class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]

        Success

        Slower than about 70% of submissions 
        More memory efficient than 84% of submissions
        """
        new_list = []
        i = 0
        j = 0
        r_len = len(A)
        c_len = len(A[0])
        for row in A:
            row.reverse()
            temp = []
            for col in row:
                if(col == 0):
                    temp.append(1)
                else:
                    temp.append(0)
            new_list.append(temp)
        return new_list