class TrieNode(object):
    def __init__(self,):
        self.children = {}
        self.isEnd = False
        self.word = None
    
class Trie(object):
    def __init__(self,):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root
        for letter in word:
            if not letter in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.isEnd = True
        node.word = word      

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []
        if not words:
            return []

        rows = len(board)
        cols = len(board[0])
        found = set()
        trie = Trie()

        for word in words:
            trie.insert(word)
        
        for i in xrange(rows):
            for j in xrange(cols):
                self.check(board, i, j, rows, cols, trie.root, set(), found)
        return found
    
    def check(self, board, i, j, rows, cols, node, visited, found):
        if node.isEnd:
            found.add(node.word)
    
        if i < 0 or i >= rows:
            return 
        if j < 0 or j >= cols:
            return
        if not board[i][j] in node.children:
            return
        
        visited.add((i,j))
        steps = [(1,0),(-1,0),(0,1),(0,-1)]
        for dx, dy in steps:
            x = i + dx
            y = j + dy
            if (x,y) in visited:
                continue
            self.check(board, x, y, rows, cols, node.children[board[i][j]], visited, found)
        visited.remove((i,j))