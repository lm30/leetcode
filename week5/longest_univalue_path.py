# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.longest = 0
    
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return self.longest
        
    def univ_helper(self, root):
        left = 0
        right = 0
        if root.left:
            side, val = self.univ_helper(root.left)
            if val == root.val: # if the value of the node is the same, continue adding this
                left = side
        if root.right:
            side, val = self.univ_helper(root.right)
            if val == root.val:
                right = side
        
        self.longest = max(self.longest, left + right) # update longest len
        return [max(left, right) + 1, root.val]