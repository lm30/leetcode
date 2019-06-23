class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        Faster than 98% submissions
        Uses less memory than 63% submissions
        """
        sent = s.lower()
        front_ptr = 0
        back_ptr = len(sent) -1
        while(front_ptr < back_ptr):
            # alt way: if pointing to non alpha num char, move pointer
            if not sent[front_ptr].isalnum():
                front_ptr+=1
            elif not sent[back_ptr].isalnum():
                back_ptr -=1
            else:
                if(sent[front_ptr] != sent[back_ptr]):
                    return False
                else:
                    front_ptr += 1
                    back_ptr -= 1
        return True