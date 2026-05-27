# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


        ### Bruteforce ###
        ## DFS preorder+sort OR inorder and then pick kth
        '''
        res = []

        def dfs(node):

            if not node:
                return 
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res[k-1]
        '''

        ### DFS count the items ###
        ## Instead of storing reduce k count 
        # Note that we need to reduce k after reaching the leftmost element since then its sorted
        #res = None
        res = None
        def dfs(node):
            
            nonlocal res, k
            if not node:
                return

            dfs(node.left)
            k -= 1
            if k == 0:
                res = node.val 
                return 
            
            if  k > 0:
                dfs(node.right)

        dfs(root)
        return res
        

        