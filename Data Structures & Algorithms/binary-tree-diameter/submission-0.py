# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        ### DFS ###
        # The idea is that the diameter of binary tree for example a three node tree is 
        # sum of left and right edge i.e. 2 
        # But its parent's diameter (say a tree above the three nodes) will be max of left right i.e 1 
        res = 0
        def diameteHelper(node):
            nonlocal res
            if not node:
                return 0
        
            left = diameteHelper(node.left)
            right = diameteHelper(node.right)

            res = max(res, left + right)

            return 1 + max(left, right)
        
        diameteHelper(root)
        return res
