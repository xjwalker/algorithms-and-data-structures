from typing import Optional
from trees.treenode import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.loop(root, subRoot)
    
    def loop(self, root, subroot):
        if root is None:
            return False
        if root.val == subroot.val:
            if self.recursive(root, subroot):
                return True
        return self.loop(root.left, subroot) or self.loop(root.right, subroot) 

    
    def recursive(self, first, second):
        if first is None and second is None:
            return True
        if first is None and second or second is None and first:
            return False
        if first.val != second.val:
            return False
        return self.recursive(first.left, second.left) and self.recursive(first.right, second.right)