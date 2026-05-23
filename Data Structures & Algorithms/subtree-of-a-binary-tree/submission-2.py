# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def _isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return self._isSameTree(root.left,subRoot.left) and self._isSameTree(root.right,subRoot.right)
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        if not root:
            return False
        
        
        if root.val == subRoot.val:
            if self._isSameTree(root,subRoot):
                return True

        left = self.isSubtree(root.left,subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right
            