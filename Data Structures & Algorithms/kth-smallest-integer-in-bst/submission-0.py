# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        ### Bruteforce ###
        # Convert the tree to array by normal traver



        ### Solution 1 ###
        # Since this is a BST we can get the sorted array by inorder DFS 
        # Return the k+1th index value as 1 index
        res = []

		# Closure Function , Recursive inorder func
        def inorder(node: Optional[TreeNode]) -> None:
        
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res[k-1]