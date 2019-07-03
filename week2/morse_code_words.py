class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        on^2
        
        Successful
        Faster than 98% submissions
        Less memory than 58% submissions
        """
        morse = {"a": ".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        total = 0
        word_list = {}
        for word in words:
            morse_equiv = []
            for letter in word:
                # make the morse equivalent
                morse_equiv += morse[letter]
            w = ''.join(morse_equiv)
            if word_list.get(w) == None:
                total += 1
                word_list[w] = 1
        return total