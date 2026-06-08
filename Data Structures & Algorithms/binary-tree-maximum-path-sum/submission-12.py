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
        # For every node, find left max and right max path sum seperately and update maxsum
        # To find the left/right max sum do path find which path is max left or right within and provide that 
        # Since node to node that means post order, repeat the post order as preorder
        # Time: O(n^2) -> from  every node we find best path sum on left and right side and then combine to update result
        # Space: O(n) -> recursive stack O(n) for each run 
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
        # Since node to node is the path sum not root to leaf, this is postorder
        # Postorder is the kind, in which we get answer from both left and right 
        # 1. Then update the answer by combining 
        # 2. But return to parent the path that is required 
        # since path sum is current node + left and right but to maintain maxsum for tree above we need to provide
        # one path and the best path will be whichever is maximum.
        # Similarly paths can be negative and we don't want that negative values in our sum so we give max of 0 or values
        # Time: O(n)
        # Space: O(n)  -> recursive stack 
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
        



        
        