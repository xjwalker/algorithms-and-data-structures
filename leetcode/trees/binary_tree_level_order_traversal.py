from typing import Optional, List
from trees.treenode import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        elements = {}
        self.recursive(root, elements, 0)
        res = []
        for level, values in elements.items():
            res.append(values)
        return res

    def recursive(self, node, elements, level=0):
        if node is None:
            return None
        if level not in elements:
            elements[level] = []
        elements[level].append(node.val)
        level += 1
        left = self.recursive(node.left, elements, level)
        right = self.recursive(node.right, elements, level)
        

        