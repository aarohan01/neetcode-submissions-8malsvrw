# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        ### DFS ###
        # Idea is that preorder gives the root node and inorder left and right give its children
        # So we can divide both arrays based on the preorder root node into left and right subtrees,
        # AS INDEX MATCHES ON BOTH ARRAYS
        # Keep doing it recursively till none 

        def dfs (inorder,preorder):

            if not preorder:
                return None

            node = TreeNode(preorder[0])
            index = inorder.index(node.val)

            node.left = dfs(inorder[:index],preorder[1:index+1])
            node.right = dfs(inorder[index+1:],preorder[index+1:])

            return node
        
        return dfs(inorder,preorder)

            

        
