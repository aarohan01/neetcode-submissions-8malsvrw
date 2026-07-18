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
            
            ## Base Case 1 - Failure
            if not node:
                return 
            
            ## Base Case 2 - Success
            if node in hashmap:
                return hashmap[node]

            ## Subproblem
            cnode = Node(node.val)
            hashmap[node] = cnode
            # Append to neighbor
            for c in node.neighbors:
                cnode.neighbors.append(dfs(c))

            # If reach end, return to parent to append in neighbors
            return cnode

        return dfs(node)