class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        
        
        Successful

        Faster than 45% submissions
        Less memory than 78% submissions
        """
        self.size = 10000
        self.list = [None] * self.size
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        hash = self._get_hash(key)
        if self.list[hash] == None:
            self.list[hash] = []
            self.list[hash].append([key, value])
        else:
            for i in self.list[hash]:
                if len(i) > 1 and i[0] == key: 
                    # if, of this pair, the key value equals key, change val
                    i[1] = value
                    return
            self.list[hash].append([key,value]) # else if hash filled but no key match, append it
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hash = self._get_hash(key)
        if self.list[hash] != None:
            for i in self.list[hash]:
                if i[0] == key:
                    return i[1] # return the value
        return -1
        
    def _get_hash(self, key):
        """
        :type key: int
        :rtype: int
        """
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        hash = self._get_hash(key)
        if self.list[hash] != None:
            j = 0
            for i in self.list[hash]:
                if i[0] == key:
                    print self.list[hash].pop(j)
                    return
                j += 1
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)