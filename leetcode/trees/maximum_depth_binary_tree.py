from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.count_level(root, 0)

    def count_level(self, node, level):
        if node is None:
            return level
        level += 1 
        return max(level, self.count_level(node.left, level), self.count_level(node.right, level))
        