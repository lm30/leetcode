class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.

        Faster than 98% submissions
        Less memory than 67% submissions
        """
        front_pt = 0
        back_pt = len(s) -1
        temp = ""
        while(front_pt < back_pt):
            temp = s[front_pt]
            s[front_pt] = s[back_pt]
            s[back_pt] = temp
            front_pt+= 1
            back_pt-= 1