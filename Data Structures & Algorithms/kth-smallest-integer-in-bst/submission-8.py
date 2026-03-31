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
        # *** This works but better way is to count down to 0 from k *** 
        '''
        count = 0
        res = root.val
		# Closure Function , Recursive inorder func
        def inorder(node: Optional[TreeNode]) -> Optional[int]:
            nonlocal count, res 
            if not node:
                return
            inorder(node.left)
            count += 1
            #print(node.val)
            if count == k :
                #print(f'c:{count} v:{node.val}')
                res = node.val
                # Stops exploring the right subtree of the node with kth value
                return
            
            # Only explores right subtree if k is not found yet otherwise stops 
            if count < k:
                inorder(node.right)
        
        inorder(root)
        return res
        '''


        ### Solution 3 ###
        # Solution 2 is correct and Optimal, this is just anothe optimal solution
        # Interative way.
        # Since recursive stack is not use we use a stack to maintain where to jump back.


        
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            print(curr.val)
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
        