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
        
        res = data.split(',')

        if res[0] == 'N' or not res:
            return None
        
        if len(res) == 1:
            return TreeNode(int(data[0]))

        index = 0
        ### Similar to Insert BST but binary tree so no check but instead use index on the array ###
        def insert():
            nonlocal index
            if res[index] == 'N':
                index += 1
                return None

            node = TreeNode(int(res[index]))

            index += 1
            node.left = insert()
            node.right = insert()

            return node
        
        
        root = insert()
        return root
            

