# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        res = []

        ### preorder DFS to serialize ###
        # Inorder doesn't work because while deserializing we don't know the root because of nulls
        def dfs(node):
            if not node:
                res.append('N')
                return 
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        print(','.join(res))
        return ','.join(res)
            

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        '''
        res = data.split(',')

        if res[0] == 'N' or not res:
            return None
        
        if len(res) == 1:
            return TreeNode(int(data[0]))

        index = 1
        ### Similar YET DIFFERENT to Insert BST but binary tree so no check but instead use index on the array ###
        ## The main difference is in BST the node positions aren't know we find the position based on value comparison
        # Here the position is known but we have to skip null
        #Read value
        #If N -> return None
        #Else create node
        #Then build left and right
        #Return node
        
        def insert(node):
            nonlocal index
            if res[index] == 'N':
                index += 1
                return None
            
            if not node:
                return TreeNode(int(res[index]))

            index += 1
            node.left = insert(node.left)
            node.right = insert(node.right)

            return node
        
        
        root = insert(TreeNode(int(res[0])))
        return root
        '''



        res = data.split(',')

        if res[0] == 'N' or not res:
            return None
        
        if len(res) == 1:
            return TreeNode(int(data[0]))

        index = 0
        def dfs():
            
            nonlocal index
            if res[index] == 'N':
                index += 1
                return None


            node = TreeNode(res[index])
            index += 1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
            

