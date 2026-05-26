# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def _isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return self._isSameTree(root.left,subRoot.left) and self._isSameTree(root.right,subRoot.right)
        else:
            return False
        '''

        ### Same logic different way of writing ###
        if not root and not subRoot:
            return True
        
        if not root or not subRoot:
            return False 
        
        if root and subRoot and root.val != subRoot.val:
            return False
        
        left = self._isSameTree(root.left,subRoot.left)
        right = self._isSameTree(root.right,subRoot.right)

        return left and right
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        ### Idea :
        ## DFS on root, if DFS completes but root.val never becomes subroot.val then return false : thus base case
        ## IF root.val become subrootval check issametree
        # _isSameTree : base case 1 -> both are none then we reached end return true
        # if one none then its false, if both not none yet values different then also false
        # if both not none and value same then check left and right subtree 
        ## if _isSameTree returns True then return True else, continue dfs on left and right subtree
        ## To parent pass on if any of left and right subtree output is True

        # Base Case -> Root DFS complete but no match to subroot
        # Since atleast one node on both trees no need to check that
        if not root:
            return False
        
        # SubProblem -> root.val == subroot.val somewhere -> check if same tree -> return to parent call 
        if root.val == subRoot.val:
            if self._isSameTree(root,subRoot):
                return True

        # Check left and right subtree
        left = self.isSubtree(root.left,subRoot)
        right = self.isSubtree(root.right, subRoot)

        # 
        return left or right
            