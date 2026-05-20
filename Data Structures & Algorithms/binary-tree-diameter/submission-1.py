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
        # But its parent's diameter (say a tree above the three nodes) will be max of left right plus edge between node and parent i.e. 1
        # Time: O(n)
        # Space: O(h)
        
        ### Stores overall maximum [State]###
        res = 0

        ### Calculate current nodes max and give appropriate to parent ###
        def diameteHelper(node):

            nonlocal res

            ### Base Case - leaf node's next will return 0 or Empty will return 0 ###
            if not node:
                return 0
        
            ### Subproblem and recursive calls ###
            ## Imagine 3 node tree's leaf node - leaf node's left and right will return 0,0
            # sum is possibly max or pass to parent, node to parent edge i.e 1 and max of left, right 
            left = diameteHelper(node.left)
            right = diameteHelper(node.right)
            # Max path could be left right no. of edges sum 
            res = max(res, left + right)

            ### Return to parent ###
            return 1 + max(left, right)
        
        diameteHelper(root)
        return res
