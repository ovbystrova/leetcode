# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None and q:
            return False
        elif q is None and p:
            return False

        if not p.val == q.val:
            return False

        elif p.left is None and q.left is None and p.right is None and q.right is None:
            return True

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
