# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        '''
        total = 0

        def leafPath(node: Optional[TreeNode], targetSum: int):
            
            nonlocal total

            if total and total > targetSum:
                return False

            if node.val == targetSum or total == targetSum:
                print('Here')
                return True

            
            total += node.val
            print(total)

            if total < targetSum:
                leafPath(node.left,targetSum)
                return 
            if total < targetSum:
                leafPath(node.right,targetSum)
                return 
            
            total -= node.val
           

        return leafPath(root,targetSum)
        '''

        ### Solution ###
        # Intuition : similar to backtracking path finding 
        # We go from targetSum/total to 0 and if in any path it reaches exactly zero return true
        # Base case -> if empty tree or if to target sum becomes negative then False
        # Base 2 -> Success case -> if leaf is reached and total/targetSum reaches 0
        # Else try left tree and right tree, backpropogate the result.
        # Add to total again, in case both fail and return false

        if not root:
            return False
        
        targetSum -= root.val
        print(f'sub {root.val} :{targetSum}')
        if not root.left and not root.right and targetSum == 0:
            return True

        if self.hasPathSum(root.left, targetSum):
            return True
        
        if self.hasPathSum(root.right, targetSum):
            return True
        
        targetSum += root.val
        print(f'add {root.val} : {targetSum}')
        return False




        