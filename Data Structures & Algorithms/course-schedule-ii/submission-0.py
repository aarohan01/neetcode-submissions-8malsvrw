class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        ### Topological Sort ###
        ## Basically 3-color-DFS + storing the after done in a array to preserve order 
        ## Reverse the resutling order to get what to execute first.
        # Check Courser Schedule 1 for 3-Color-DFS

        # Adj list from edge list 
        # n is given, so not missing disconnected components
        adj = { i : [] for i in range(numCourses)}

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
        return res