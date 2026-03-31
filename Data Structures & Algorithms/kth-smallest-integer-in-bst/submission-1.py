# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        ### Bruteforce ###
        # Convert the tree to array by normal traversal use say preorder trave
        '''
        res = []
        
		# Closure Function , Recursive inorder func
        def dfs(node: Optional[TreeNode]) -> None:
        
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        res.sort()
        return res[k-1]
        '''

        ### Solution 1 ###
        # Since this is a BST we can get the sorted array by inorder DFS 
        # Return the k-1th index value as 1 index
        '''
        res = []
        
		# Closure Function , Recursive inorder func
        def inorder(node: Optional[TreeNode]) -> None:
        
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        inorder(root)
        return res[k-1]
        '''

        ### Solution 2 ###
        # If we create an array with inorder, it will take additional storage and also has to 
        # visit every node EVERYTIME.
        # Although worst case time and space complexity will be same for that version as well i.e O(n)
        # But instead we can keep a count and stop at the kth element. This is more optimal.

        count = 0
        res = root.val
		# Closure Function , Recursive inorder func
        def inorder(node: Optional[TreeNode]) -> Optional[int]:
            nonlocal count, res 
            if not node:
                return
            inorder(node.left)
            count += 1
            if count == k :
                print(f'c:{count} v:{node.val}')
                res = node.val
                return
            inorder(node.right)
        
        inorder(root)
        return res

