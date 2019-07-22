from Queue import Queue
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        Successful
        """
        self.que = Queue()
        self.que2 = Queue()
        
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.que.put(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while self.que.qsize() > 1: # while something left in teh queue
            self.que2.put(self.que.get()) # put it in queue 2
        if self.que.qsize() == 1: # switch them back
            res = self.que.get()
            temp = self.que
            self.que = self.que2
            self.que2 = temp
            return res
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while self.que.qsize() > 1: # while something left in teh queue
            self.que2.put(self.que.get()) # put it in queue 2
        if self.que.qsize() == 1: 
            res = self.que.get()
            temp = self.que
            self.que2.put(res)
            self.que = self.que2 
            self.que2 = temp
            return res
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.que.qsize() + self.que2.qsize() == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()