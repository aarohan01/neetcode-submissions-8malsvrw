# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        

        ### Bruteforce ###
        ## THE BRUTEFORCE VERSION IS MORE COMPLICATED THAN OPTIMAL
        # For every node, find max path (postorder) and return it, do this for every node.
        # Since node to node that means post order, repeat the post order as preorder
        '''
        maxsum = float('-inf')
        def dfs(node):

            nonlocal maxsum 
            if not node:
                return 

            left = getMaxPathSum(node.left)
            right = getMaxPathSum(node.right)

            maxsum = max(maxsum, node.val + left + right)

            dfs(node.left)
            dfs(node.right)

        ### The actual postorder calculating max path sum ###
        def getMaxPathSum(node):

            if not node:
                return 0

            left = getMaxPathSum(node.left)
            right = getMaxPathSum(node.right)

            return max(0, node.val + left, node.val + right)

        dfs(root)
        return maxsum

        '''

        ### DFS postorder - Optimal ###
        maxsum = float('-inf')
        
        def dfs(node):

            nonlocal maxsum

            # Base case
            if not node:
                return 0

            # Subproblem is that find the right and left pathsum
            # It can be negative as well so left and right max will be either left, right or 0
            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)

            # Postorder combine 
            maxsum = max(maxsum, node.val + left + right)

            # Return to parent the best path
            return max(node.val+ left, node.val+ right)
        
        dfs(root)
        return maxsum
        



        
        