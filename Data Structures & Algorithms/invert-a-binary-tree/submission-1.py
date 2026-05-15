# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # No closure or private method needed for recursion since the parent method has all the required arguments
        

        ### DFS - recursively swap ###
        # For leaf or empty node return None
        # Else swap and recursively do that for left and right subtree
        # Once complete return the root
        # Time: O(n) 
        # Space: O(h) but worse is O(n) where h is height and this is for recursive stack

        ### Base Case ###
        if not root:
            return None
        
        # Action
        root.left, root.right = root.right, root.left
        
        # Recursion
        self.invertTree(root.left)
        self.invertTree(root.right)

        # When all calls return then og root 
        return root
