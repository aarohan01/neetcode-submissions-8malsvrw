# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:



        res = []
        def dfs(node):

            if not node:
                return 
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        
        dfs(root)

        #return res == sorted(set(res)) 
        #OR
        for i in range(1,len(res)):
            if res[i-1] >= res[i]:
                return False
        return True


        '''
        def dfs(node,leftbound,rightbound):

            if not node:
                return True

            if not (leftbound < node.val < rightbound):
                return False

            left = dfs(node.left,leftbound, node.val)
            right = dfs(node.right,node.val,rightbound)

            return left and right
        
        return dfs(root,float('-inf'),float('inf'))
        '''
        