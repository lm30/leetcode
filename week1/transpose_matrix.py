class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        new_array = []
        i = 0 # row
        j = 0 # col
        c_length = len(A[0])
        r_length = len(A)
        for i in range(c_length): # for each row
            row_list = [] # create a list to hold the elements in the row
            for j in range(r_length): # go through the individual elements by col
                row_list.append(A[j][i]) # find the tranpose
            new_array.append(row_list) # append the row to the array
        return new_array