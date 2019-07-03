class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        
        Successful

        Faster than 43% submissions
        Less memory than 88% submissions
        """
        self.size = 10000
        self.list = [None] * self.size
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash = self._get_hash(key)
        if self.list[hash] == None:
            self.list[hash] = []
            self.list[hash].append(key)
        else:
            for i in self.list[hash]:
                if i == key:
                    return
            self.list[hash].append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash = self._get_hash(key)
        if self.list[hash] != None:
            idx = 0
            for i in self.list[hash]:
                if i == key:
                    del self.list[hash][idx]
                    return
                idx += 1
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hash = self._get_hash(key)
        if self.list[hash] != None:
            for i in self.list[hash]:
                if i == key:
                    return True
        return False
    
    def _get_hash(self, key):
        """
        :type key: int
        :rtype: int
        """
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)