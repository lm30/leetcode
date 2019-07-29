# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left = [root.val, 0] # value and height b/c only want output val
        self.bottom_helper(root, left, 0)
        return left[0]
        
    def bottom_helper(self, root, left, height):
            if root == None:
                return
            
            if height > left[1]: # if teh height is greater than left's
                left[0] = root.val # this is the new left[]
                left[1] = height
            
            self.bottom_helper(root.left, left, height + 1)
            self.bottom_helper(root.right, left, height + 1)