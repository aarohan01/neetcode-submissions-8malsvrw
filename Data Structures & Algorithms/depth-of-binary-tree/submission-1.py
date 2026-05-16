# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        ### DFS ###
        # Take a 3 node tree and then 
        # Base case : after leaf or no tree will give 0
        # Subproblem & recursive call is that we want depth of max (left and right) subtree
        # Return to parent : 1 + max of subtree
        # Time: O(n)
        # Space: O(h)
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left,right)

