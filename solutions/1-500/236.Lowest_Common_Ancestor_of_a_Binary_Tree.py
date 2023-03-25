from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        cache = defaultdict(list)
        cache[root].append(root)
        cache.update(self.find_node(
            root, 
            -1, 
            cache
            ))
        cache.update(self.find_node(
            root.right,
            root,
            cache
            ))
        path_p = cache[p]
        path_q = cache[q]

        for i in range(len(path_p)-1, -1, -1):
            if path_p[i] in path_q:
                return path_p[i]

        return 0

    def find_node(self, root, parent, cache):

        if root is None:
            return cache

        path = cache[parent]
        cache[root].extend(path)
        cache[root].append(root)

        cache.update(self.find_node(root.left, root, cache))
        cache.update( self.find_node(root.right, root,cache))

        return cache
