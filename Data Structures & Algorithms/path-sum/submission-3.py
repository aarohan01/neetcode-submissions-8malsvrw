# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        
        ### Solution ###
        # Intuition : similar to backtracking path finding 
        # We go from targetSum/total to 0 and if in any path it reaches exactly zero return true
        # Base case -> if empty tree, previously added condition for targetSum  < 0 but
        # since the numbers itself can be negative cannot use this.
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
   
        
        '''
        ### Solution 2 ### Iterative ###
        # Solution 1 works but is iterative 
        # Same concept but will need a stack
        stack = []
        total = 0

        if not root:
            return False 
        
        curr = root
        while True:
            stack.append(curr)
            total += curr.val

            if not curr.left and not curr.right and total == targetSum:
                return True
            
            if curr and curr.left:
                curr = curr.left 
        '''




        