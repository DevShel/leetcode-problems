from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if (root):
            temp = root.right
            root.right = root.left
            root.left = temp

            root.left = self.invertTree(root.left)
            root.right = self.invertTree(root.right)
        return root