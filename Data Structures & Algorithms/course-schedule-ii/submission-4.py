from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        ### Topological Sort - DFS - Representation by dependency ###
        ## Basically 3-color-DFS + storing the after done in a array to preserve order 
        ## No need to reverse the result order since we are doing Dependency Representation + DFS
        # Check Courser Schedule 1 for 3-Color-DFS
        # Time: O(V+E) -> adj list construction and dfs 
        # Space: O(V+E)

        # Adj list from edge list 
        # n is given, so not missing disconnected components
        adj = { i : [] for i in range(numCourses)}

	    ### Construting Representation by dependency ###
        for course, prereq in prerequisites:
            adj[course].append(prereq)

        #print(f'Adj : {adj}\n')
    
        # DFS to check cycle
        visiting = set()
        done = set()
        res = []

        def dfs(node):

            # Base case : Cycle -  if the node is already visiting 
            # basically if next nodes neighbors list also contains its parent which we visited already 
            if node in visiting:
                return True 

            # Base case : No Cycle - if the node has no prereq 
            if node in done:
                return False

            # Subproblem
            # If node not visiting
            visiting.add(node)

            # Check the neighbors
            for nei in adj[node]:
                # Return Aggregation
                if dfs(nei):
                    # Optional cleanup the visiting set of all node till the parent since we are terminating 
                    # early and might not hit the visiting.remove(node) in case of Failure
                    # visiting.
                    #visiting.remove(node)
                    return True 
            

            # Backtracking to check cycle in another part  
            visiting.remove(node)

            # White/Gray/Black concept instead of memoization
            # Unvisited, Visiting and Done visiting 
            # Basically if subgraph is already explored once we know that there is no cycle from that node.
            # From that node its always gonna hit base case of success
            done.add(node)
            res.append(node)
            # If base case is hit in child backpropagate true
            return False 

        # To cover all disconnected componenets
        for node in range(numCourses):
            # Skip if node already done in a dfs
            if node not in done:
                # If cycle then false
                if dfs(node):
                    return []
        
        ### Since we constructed using dependency we don't need to reverse ###
        return res
        



        ### Topological Sort - BFS Multisource Kahn's - Representation by dependency ###
        ## Basically BFS but pop only one at a time in queue
        ## Reverse the resutling order to get what to execute first. (Dependency Representation + BFS) or use order representation
        # Time: O(V+E) -> adj list construction and bfs
        # Space: O(V+E)

        # Adj list from edge list 
        # n is given, so not missing disconnected components
        adj = { i : [] for i in range(numCourses)}
        indegrees = {i:0 for i in range(numCourses)}
	    ### Construting Representation by dependency ###
        # course -> prereq
        for course, prereq in prerequisites:
            adj[course].append(prereq)
            indegrees[prereq] += 1


        print(f'Adj : {adj}\n')
        print(f'Indegrees : {indegrees}\n')


        ### Queue ###
        queue = deque()
        # Add to queue all nodes with indegree 0 (multisources)
        for i in indegrees:
            if indegrees[i] == 0:
                queue.append(i)


        res = []
        level = 0
        # BFS only one node at a time
        while queue:
            
            for q in range(len(queue)):
                node = queue.popleft()

                res.append(node)

                for nei in adj[node]:

                    indegrees[nei] -= 1
                    if indegrees[nei] == 0:
                        queue.append(nei)
            level += 1

        ## If all nodes not present in result, then there was a cycle 
        # There are still nodes that have indegree more than 0
        if len(res) != len(adj):
            return []
        return res[::-1]
