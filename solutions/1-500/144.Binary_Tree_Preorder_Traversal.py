from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Approach 1: Recursive
        # if root is None:
        #     return []

        # return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

        # Approach 2: Iterative

        answer = []
        stack = [root]

        if root is None:
            return []

        while len(stack) != 0:
            current = stack.pop()
            if current is not None:
                answer.append(current.val)
                stack.append(current.right)
                stack.append(current.left)

        return answer
