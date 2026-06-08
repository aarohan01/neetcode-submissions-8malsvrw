# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        ### DFS ###
        # Idea is that preorder gives the root node and inorder left and right give its children
        # So we can divide both arrays based on the preorder root node into left and right subtrees,
        # Keep doing it recursively till none 
        # Time: O(n^2)  -> for every node we also do linear search in array
        # Space: O(n^2) -> for every node we store the entire array n*n + n (recursion stack)
        '''
        def dfs (inorder,preorder):
            
            ## Base case
            if not preorder:
                return None

            ## Subproblem
            # Create a node
            node = TreeNode(preorder[0])
            # Index
            index = inorder.index(node.val)

            ## combine
            node.left = dfs(inorder[:index],preorder[1:index+1])
            node.right = dfs(inorder[index+1:],preorder[index+1:])
            
            ## Return to parent when base case not hit
            return node
        
        return dfs(inorder,preorder)
        '''

        ### DFS - precompute index in inorder + instead of creating array pass index ###
        ## We are traversing preorder on by one but bounds are for inorder since we split inorder
        # We check every preorders value's index in the inorder array, instead we can store mapping of index:val 
        # inside the inorder as a lookup, no need for looking preorder value.
        # Instead of passing the array we can pass the index values

        ## Inefficeint : n^2 ##
        '''
        #This is checking for every preorder value the index
        hashmap = {}
        for i in preorder:
            hashmap[i] = inorder.index(i)
        print(hashmap)
        '''
        # Since we just need a mapping of what value is at what index not really in order of preorder any order is fine
        hashmap = {val:idx for idx,val in enumerate(inorder)}

        pre_idx = 0
        def dfs (in_start, in_end):
            
            nonlocal pre_idx
            ## Base case
            if in_start > in_end:
                return None

            ## Subproblem
            # Create a node
            node = TreeNode(preorder[pre_idx])
            pre_idx += 1
            # Index in inorder, which will be mid as its inorder
            mid_idx = hashmap[node.val]

            ## combine
            node.left = dfs(in_start,mid_idx-1)
            node.right = dfs(mid_idx+1,in_end)
            
            ## Return to parent when base case not hit
            return node
        
        return dfs(0,len(inorder)-1)

        
