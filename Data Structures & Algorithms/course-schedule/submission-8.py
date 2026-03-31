class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        ### Solution ###
        ### Version 1 : using memoization and optional cleanup ###
        ''' 
        # Given edges we need to build adj list graph of directed edges.
        # Note here that some might not be in pre-requisite but numCourses is a range of courses
        adj = { i : [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adj[course].append(prereq)

        print(f'Adj : {adj}\n')
    
        # DFS to check cycle
        visiting = set()

        def dfs(node, visiting):

            print(f'Node :{node}')
            # Base case : Failure -  if the node is already visiting 
            # basically if next nodes neighbors list also contains its parent which we visited already 
            if node in visiting:
                return False 

            # Base case : Success - if the node has no prereq 
            if adj[node] == []:
                return True

            # If node not visiting
            visiting.add(node)

            # Check the neighbors
            for nei in adj.get(node):
                # If dfs returns False return False 
                if not dfs(nei,visiting):
                    # Optional cleanup the visiting set of all node till the parent since we are terminating 
                    # early and might not hit the visiting.remove(node) in case of Failure
                    # visiting.
                    visiting.remove(node)
                    return False 
            

            # Backtracking to check cycle in another part  
            visiting.remove(node)

            # Memoization : If we determine that from a node we don't get cycle set it to Success base case 
            # So that when some other nodes neighbor is this node, we don't check neighbors again 
            adj[node] = []

            # If base case is hit in child backpropagate true
            return True 

        ### For the result to be True no instance of dfs should return False ###
        # If any return false return false immediatedly else after return True
        for i in range(numCourses):
            if dfs(i, visiting) == False:
                return False
        return True
        '''

        ### Version 2 : using another set called done to keep track of successful path ###

        # Given edges we need to build adj list graph of directed edges.
        # Note here that some might not be in pre-requisite but numCourses is a range of courses
        adj = { i : [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            adj[course].append(prereq)

        print(f'Adj : {adj}\n')
    
        # DFS to check cycle
        visiting = set()
        done = set()

        def dfs(node, visiting):

            print(f'Node :{node}')
            # Base case : Failure -  if the node is already visiting 
            # basically if next nodes neighbors list also contains its parent which we visited already 
            if node in visiting:
                return False 

            # Base case : Success - if the node has no prereq 
            if node in done:
                return True

            # If node not visiting
            visiting.add(node)

            # Check the neighbors
            for nei in adj.get(node):
                # If dfs returns False return False 
                if not dfs(nei,visiting):
                    # Optional cleanup the visiting set of all node till the parent since we are terminating 
                    # early and might not hit the visiting.remove(node) in case of Failure
                    # visiting.
                    visiting.remove(node)
                    return False 
            

            # Backtracking to check cycle in another part  
            visiting.remove(node)

            # White/Gray/Black concept instead of memoization
            # Unvisited, Visiting and Done visiting 
            # Basically if subgraph is already explored once we know that there is no cycle from that node.
            # From that node its always gonna hit base case of success
            done.add(node)

            # If base case is hit in child backpropagate true
            return True 

        ### For the result to be True no instance of dfs should return False ###
        # If any return false return false immediatedly else after return True
        for i in range(numCourses):
            if dfs(i, visiting) == False:
                return False
        return True

