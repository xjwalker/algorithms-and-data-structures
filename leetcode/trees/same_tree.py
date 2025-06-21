from typing import Optional
from trees.treenode import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.recursive(p, q)

    def recursive(self, first, second):
        if first is None and second is None:
            return True
        if first is None and second or second is None and first:
            return False
        if first.val != second.val:
            return False
        return self.recursive(first.left, second.left) and self.recursive(first.right, second.right)

    