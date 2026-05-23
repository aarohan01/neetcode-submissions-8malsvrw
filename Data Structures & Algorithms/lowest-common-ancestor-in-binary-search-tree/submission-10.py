# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:


        ### DFS ###
        # This is BST not binary tree so comparision of value is important.
        # Given : p and q will exist and also atleast 2 nodes will exist. p or q can also be ancestor
        # LCA is the lowest in the tree where p and q are children
        # BST properties -> parent/LCA will be inbetween the children thus till both values greater or lower than 
        # parent DFS.
        # Its like binary search :
        # if both are lower then check the left subtree 
        # if both are greater then check the right subtree
        # else some is equal or split then return root
        

        if not root:
            return None

        if min(p.val,q.val) > root.val:
            #return is important
            #res = self.lowestCommonAncestor(root.right,p,q)
            # OR
            return self.lowestCommonAncestor(root.right,p,q)
        elif max(p.val,q.val) < root.val:
            #res = self.lowestCommonAncestor(root.left,p,q)
            #OR
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            ## Inclues cases - 
            #1. p or q val equal to root.val 
            #2. p <root< q or q <root<p
            return root
        
        #return res

