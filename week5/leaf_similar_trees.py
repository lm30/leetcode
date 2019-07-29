# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        leaves1 = []
        leaves2 = []
        self.find_leaves(root1, leaves1)
        self.find_leaves(root2, leaves2)
        
        return leaves1 == leaves2
        
    def find_leaves(self, root, leaves):
        if root is None:
            return None
        if root.left is None and root.right is None: # is leaf
            leaves.append(root.val)
            
        self.find_leaves(root.left, leaves)
        self.find_leaves(root.right, leaves)