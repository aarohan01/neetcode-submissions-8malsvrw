class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


        # Given is Adj Edge List 
        # Making Adj List 

        visited = {}

        def dfs(node):

            if not node:
                return None
            
            if node in visited:
                return visited[node]

        
            cnode = Node(node.val)
            visited[node] = cnode

            for c in node.neighbors:
                cnode.neighbors.append(dfs(c))

            return cnode

        return dfs(node)