"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


        hashmap = {}
        

        def dfs(node):

            if not node:
                return None

            if node in hashmap:
                return hashmap[node]
            
            new_node = Node(node.val)
            hashmap[node] = new_node

            for nei in node.neighbors:
                new_nei = dfs(nei)
                if new_nei:
                    new_node.neighbors.append(dfs(nei))

            return new_node


        return dfs(node)
        


