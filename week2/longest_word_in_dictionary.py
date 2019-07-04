# source from https://www.geeksforgeeks.org/trie-insert-and-search/
class TrieNode: 
    # Trie node class 
    def __init__(self): 
        self.children = {}
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False

class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root = self.getNode() 
        
    def getNode(self): 
        # Returns new trie node (initialized to NULLs) 
        return TrieNode() 
    
    def insert(self,key): 
        curr = self.root 
        for c in key: 
            if c not in curr.children: 
                curr.children[c] = TrieNode()
            curr = curr.children[c] 
        curr.isEndOfWord = True
    def find_longest_word(self):
        return self._longest_word(self.root, "")
    
    def _longest_word(self, node, result):
        res = result
        for c, ch in node.children.items():
            if ch.isEndOfWord:
                x = self._longest_word(ch, res + c)
                if len(x) > len(res):
                    res = x
                elif len(x) == len(res) and ord(x) < ord(res):
                    res = x
        return res
        
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        t = Trie()
        for w in words:
            t.insert(w)
        return t.find_longest_word()