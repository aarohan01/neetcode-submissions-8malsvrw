class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


        ### Hashmap + DFS normal coverage on adj list ###
        ## Only the start node is given
        # we need to keep creating every node in the neighbors
        # If neighbors already exist we need to give back.
        # But to track the already created node we need to map old and new nodes.


        visited = {None:None}

        def dfs(node):
            
            if node in visited:
                return visited[node]

        
            cnode = Node(node.val)
            visited[node] = cnode

            for c in node.neighbors:
                cnode.neighbors.append(dfs(c))

            return cnode

        return dfs(node)