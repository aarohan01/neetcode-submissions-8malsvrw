# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, csum):
            
            if not node:
                return False

            csum += node.val

            if not node.left and not node.right and csum == targetSum:
                return True

            left = dfs(node.left, csum)
            right = dfs(node.right, csum)

            return left or right

        return dfs(root, 0) 