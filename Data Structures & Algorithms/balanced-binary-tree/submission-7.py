# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        ### intuition 
        # difference between left and right 
        # return 1 to parent tree
        # three node example - 

        maxdiff = 0
        def balancedBinary(node):
            
            nonlocal maxdiff
            if not node:
                return 0

            
            left = balancedBinary(node.left)
            right = balancedBinary(node.right)

            maxdiff = max(maxdiff,abs(left-right))

            return 1 + max(left,right)

        balancedBinary(root)
        return False if maxdiff > 1 else True

            
        