# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        '''
        maxdiff = 0
        def checkMaxDiff(node):
            
            nonlocal maxdiff

            if not node:
                return 0
            
            left = checkMaxDiff(node.left)
            right = checkMaxDiff(node.right)

            maxdiff = max(maxdiff, abs(left - right))

            return 1 + max(left,right)

        checkMaxDiff(root)
        return False if maxdiff > 1 else True
        '''

        #maxdiff = 0
        def checkMaxDiff(node):
            
            #nonlocal maxdiff

            if not node:
                return 0
            
            left = checkMaxDiff(node.left)
            if left == -1:
                return -1

            right = checkMaxDiff(node.right)
            if right == -1:
                return -1
                
            diff = abs(left - right)
            if diff > 1:
                return -1

            return 1 + max(left,right)

        return False if checkMaxDiff(root) == -1 else True
        

