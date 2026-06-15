# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        ### Recursion ###
        '''
        res = []
        def preorder(node):
            
            if not node:
                return None
        
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return res
        '''

        ### Iteration ###
        stack = []
        res = []
        curr = root

        while stack or curr:
            print(res)
            while curr:
                stack.append(curr)
                res.append(curr.val)
                curr = curr.left
            curr = stack.pop()
            curr = curr.right

        return res

        