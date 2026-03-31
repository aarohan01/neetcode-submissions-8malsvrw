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
        
        ## Need to draw and visualize and check this to understand ##
        # Ex : Tree = [7,5,9,4,6,8,10] , Preorder = [7,5,4,6,9,8,10], Inorder = [4,5,6,7,8,9,10]
        # Left subtree : the left subtree will be from the 1st element of preorder list, 0 is the root
        # to mid. and the indexes required from inorder will be upto mid
        # 7 is root, index in inorder = 3, since inorder splits into left and right, we know 4,5,6 forms left subtree
        # in pre-order that maps to 1 to 3 i.e 1 to mid index of inorder. Plus for future left tree
        # apart from current root index i.e mid 
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])

        # Right subtree :
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root

