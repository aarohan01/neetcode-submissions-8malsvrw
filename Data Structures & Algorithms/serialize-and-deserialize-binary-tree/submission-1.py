# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        if not root:
            return 'N'

        res = []
        queue = deque()
        queue.append(root)

        while queue:

            for q in range(len(queue)):

                node = queue.popleft()

                if not node:
                    res.append('N')
                    continue
                
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            
        print('#'.join(res))
        return '#'.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if (len(data) == 1 and data[0] == 'N') or not data:
            return 

        if len(data) == 1:
            return TreeNode(int(data[0]))

        
        res = data.split('#') 
        print(res)

        root = TreeNode(int(res[0]))
        queue = deque()
        queue.append(root)
        index = 1
        while queue:

            for i in range(len(queue)):

                node = queue.popleft()
                node.left = TreeNode(int(res[index])) if res[index] != 'N' else None
                if res[index] != 'N':
                    queue.append(node.left)
                index += 1

                node.right = TreeNode(int(res[index])) if res[index] != 'N' else None
                if res[index] != 'N':
                    queue.append(node.right)
                index += 1
        return root



