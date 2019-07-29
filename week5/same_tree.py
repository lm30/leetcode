# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.search_tree(p, q)
    
    def search_tree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if (root1 is None and root2 is not None) or (root2 is None and root1 is not None):
                # if leaf and not leaf for root 1 or 2
                return False
        else:
            if root1.val == root2.val:
                # and is important b/c need both vals to be true
                return self.search_tree(root1.left, root2.left) and self.search_tree(root1.right, root2.right)
            else:
                return False