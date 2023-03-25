import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        min_value = -math.inf
        max_value = math.inf

        def validate(root, min_value, max_value):

            if root is None:
                return True

            if root.val <= min_value or root.val >= max_value:
                return False

            return validate(root.left, min_value, root.val) and validate(root.right, root.val, max_value)

        return validate(root, min_value, max_value)
