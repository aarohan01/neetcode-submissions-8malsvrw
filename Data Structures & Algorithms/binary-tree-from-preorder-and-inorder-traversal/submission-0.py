# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        

        ### Solution 1 : suboptimal ###
        # NOTE THAT THIS IS BINARY TREE NOT BST, so inorder is not sorted.
        # After looking at the solution, the video gives a suboptimal solution 
        # Preorder - Visit root, left subtree, right subtree
        # Inorder - Left subtree, Visit root, right subtree
        # So Pre-order gives root, while inorder can be used to determine left right subtrees
        # Idea is that search root in preorder, then sub


        # Base case : if preorder or inorder subarray is empty then return none 
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)

        # Left subtree :
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid+1])

        # Right subtree :
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

