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
        # Since node to node that means post order

        maxsum = float('-inf')
        def dfs(node):
            
            nonlocal maxsum
            # Base case
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            
            leftmax, rightmax = max(left,0), max(right,0)
            maxsum = max(maxsum, node.val + leftmax + rightmax)


            return max(node.val+leftmax, node.val+rightmax)

        
        def repeat(node):

            if not node:
                return 

            dfs(node)
            repeat(node.left)
            repeat(node.right)
        
        repeat(root)
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



        
        