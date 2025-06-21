from typing import Optional
from trees.treenode import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.recursive(root)

    def recursive(self, node):
        if node is None:
            return
        left = self.recursive(node.left)
        right = self.recursive(node.right)
        node.left = right
        node.right = left
        return node
