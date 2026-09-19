# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        

        ### Bruteforce ###
        # O(n)
        # O(n)
        '''
        res = []
        def dfs(node):

            if not node:
                return 

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        print(res)
        return res[k-1]
        '''

        ### Idea ###
        # Reach left most then increment counter if it reaches k return 
        counter = 0
        res = None
        def dfs(node):
            nonlocal counter, res
            if not node or res is not None:
                return 


            dfs(node.left)
            if res is not None:
                return 
            counter += 1
            if counter == k:
                res = node.val
                return 
            dfs(node.right)

        dfs(root)
        return res
        

