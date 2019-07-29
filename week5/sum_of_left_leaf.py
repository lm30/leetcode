# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.sum_helper(root, res)
        return sum(res)
    
    def sum_helper(self, root, sum):
        if root is None:
            return root
        if root.left and not root.left.left and not root.left.right: 
            # is leaf with no children
            sum.append(root.left.val)
        self.sum_helper(root.left, sum)
        self.sum_helper(root.right, sum)