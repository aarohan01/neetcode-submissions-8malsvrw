class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        ### Solution ###
        # Given edges we need to build adj list graph of directed edges.

        # Edge case : Empty prereq
        if not prerequisites:
            return True

        # Building the graph representation as adj list
        adj = {}
        for src, dst in prerequisites:
            if src not in adj:
                adj[src] = []
            if dst not in adj:
                adj[dst] = []
            adj[src].append(dst)

        print(f'Adj : {adj}\n')

        
        # DFS to check cycle
        visited = set()

        def dfs(node, visited):

            print(f'Node :{node}')
            # Base case : Failure -  if the node is already visited 
            if node in visited:
                print(f'Returning False')
                return False 

            # Base case : Success - if the node has no prereq 
            if adj.get(node) == []:
                return True

            # If node not visited
            visited.add(node)

            # Check the neighbors
            for nei in adj.get(node):

                print(f'Neighor :{nei}')
                if not dfs(nei,visited):
                    visited.remove(node)
                    return False 
            
            visited.remove(node)
            #adj[node] = []
            # Backtracking to check cycle in another part 
            return True 

        ### For the result to be True no instance of dfs should return False ###
        # If any return false return false immediatedly else after return True
        for i in range(numCourses):
            if i in adj:
                if dfs(i, visited) == False:
                    return False
        return True