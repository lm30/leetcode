# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.longest_len = 0
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diam_helper(root)
        return self.longest_len
        
    def diam_helper(self, root):
        if root is None:
            return 0
        left = self.diam_helper(root.left)
        right = self.diam_helper(root.right)
        
        self.longest_len = max(self.longest_len, left + right) # update longest len
        return max(left, right) + 1 