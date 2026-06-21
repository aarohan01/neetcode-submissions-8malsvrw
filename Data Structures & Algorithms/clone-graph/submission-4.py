class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:


        ### Hashmap + DFS normal coverage on adj list ###
        ## Only the start node is given
        # we need to keep creating every node in the neighbors
        # If neighbors already exist we need to give back.
        # But to track the already created node we need to map old and new nodes.
        # Similar to linked list clone problem
        # Idea : 
        # Start with the node given, base cases are no node given or node in visited 
        # Else create node and add it to the hashmap 
        # Then repeat for neighbors while adding to current copy node.
        # Return the copy node to parent as its copied in parent's neighors list
        # Time: O(V+E) -> traverse a adj list
        # Space: O(V) -> Hashmap and recursion stack

        # Hashmap to map old and new nodes
        hashmap = {}

        def dfs(node):
            
            # Base Case 1 - if no node
            if not node:
                return 
            
            if node in hashmap:
                return hashmap[node]

        
            cnode = Node(node.val)
            hashmap[node] = cnode

            for c in node.neighbors:
                cnode.neighbors.append(dfs(c))

            return cnode

        return dfs(node)