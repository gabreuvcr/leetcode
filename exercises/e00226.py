#https://leetcode.com/problems/invert-binary-tree/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return

        self.invert_tree(root.left)
        self.invert_tree(root.right)

        root.left, root.right = root.right, root.left

        return root