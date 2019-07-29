"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        res = []
        stack = []
        curr = root
        while True:
            if curr:
                left = None
                if curr.children:
                    stack.extend(reversed(curr.children)) # add children to stack
                    left = stack.pop() # go through left then right
                stack.append(curr) # add node to go through later
                curr = left
            elif stack:
                curr = stack.pop() # take this node off the stack and see if it has children
                if curr.children and stack: # if can go further down, take from stack
                    nextNode = stack.pop()
                    if nextNode in curr.children:
                        stack.append(curr) # if is child, add to stack and nextnode is curr
                        curr = nextNode
                    else: 
                        stack.append(nextNode) 
                        res.append(curr.val)
                        curr = None
                else:
                    res.append(curr.val)
                    curr = None
            else:
                break
        return res