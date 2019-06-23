class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str

        Successful

        Faster than 73% of submissions
        Uses less memory than 25% of submissions
        """
        vowels = 'aeiouAEIOU'
        front_pt = 0
        back_pt = len(s) -1
        temp = ""
        new_s = list(s)
        while(front_pt < back_pt):
            if(new_s[front_pt] not in vowels):
                front_pt += 1
            if(new_s[back_pt] not in vowels):
                back_pt -= 1
            if(new_s[front_pt] in vowels and new_s[back_pt] in vowels):
                temp = new_s[front_pt]
                new_s[front_pt] = new_s[back_pt]
                new_s[back_pt] = temp
                
                front_pt+= 1
                back_pt-= 1
        return "".join(new_s)