# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        

        ### Bruteforce ###
        ## From every node to every node we calculate 
        # Since node to node that means post order, repeat the post order as preorder

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
        maxsum = float('-inf')
        
        def dfs(node):

            nonlocal maxsum

            if not node:
                return 0

            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)

            maxsum = max(maxsum, node.val + left + right)

            return max(node.val+ left, node.val+ right)
        
        dfs(root)
        return maxsum
        '''



        
        