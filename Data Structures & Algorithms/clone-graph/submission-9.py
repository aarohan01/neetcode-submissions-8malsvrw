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



        ### BFS (old) ###
        # The Question only gives representation of graph, the input is going to be only a single starting node
        # Given : Undirected conncected connected graph -> all nodes reachable from all nodes
        # no duplicate nodes
        # INPUT - First Node in Adj List 
        # OUTPUT - First Node of our graph  
        # VALUES - same as it index(starting from 1)

        # Either of BFS and DFS can be used
        # Using BFS + HashMap ( to maintain )
        # We maintain a hashmap to note which nodes are already created.
        '''
        
        ## Edge case - No node;
        if not node:
            return None
        
        ## Setup ## 
        # To maintain mapping
        nodeMap = {}
        # BFS 
        queue = deque()
        new = Node(node.val)
        nodeMap[node] = new
        # OG node to explore
        queue.append(node)
    
        

        print(f'First Node - Nodes: {nodeMap} Queue: {queue}')

        while len(queue) > 0:

                # No need to maintain level so skipping the loop 

                curr = queue.popleft()

                # We do not know the target, so we skip that check 

                # We loop through neighbors and check if they are already created
                for n in curr.neighbors:
                    if n not in nodeMap:
                        
                        # Create if not created
                        
                        print(f'Creating : {n.val}')
                        nodeMap[n] = Node(n.val)

                        # Explore OG node children
                        queue.append(n)
                    
                    # We created children but didn't add to neigbors of new node
                    nodeMap[curr].neighbors.append(nodeMap[n])



                        

        return nodeMap[node]
        '''
