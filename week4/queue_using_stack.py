class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        
        Successful
        """
        self.stack = []
        

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        temp = []
        while self.stack: # put all vals into temp
            temp.append(self.stack.pop())
        ret_val = temp.pop() # get the last ele (first in stack) to return
        while temp:
            self.stack.append(temp.pop())
        return ret_val
        

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        temp = []
        while self.stack: # put all vals into temp
            temp.append(self.stack.pop())
        ret_val = temp[-1] # get the last ele (first in stack) to return but doesn't rm it
        while temp:
            self.stack.append(temp.pop())
        return ret_val
        

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stack == []
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()