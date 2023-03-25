from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        left_tree = self.dfs(root.left, list(), "left_to_right")
        right_tree = self.dfs(root.right, list(), "right_to_left")

        return left_tree == right_tree

    def dfs(self, root, tree, order):

        if root is None:
            tree.append(None)
            return tree
        tree.append(root.val)

        if order == "left_to_right":
            self.dfs(root.left, tree, order)
            self.dfs(root.right, tree, order)
        elif order == "right_to_left":
            self.dfs(root.right, tree, order)
            self.dfs(root.left, tree, order)

        return tree
