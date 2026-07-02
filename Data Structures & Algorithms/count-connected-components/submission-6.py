class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        ### DFS normal coverage multicell ###
        ## Source not given can be disconnected - multicell
        ## Need to visit once every node - normal coverage
        # Idea : 
        # Make adj list from edges
        # There might be some nodes with no edges, since n is given 
        # DFS on the adj list based on cells not visited
        # Initialize components as n - len(adj) coz remainining single nodes count as component
        # For every successful dfs we have a component 
        # Time: O(V+E) -> DFS
        # Space: O(V+E) -> adj list
        '''
        # Edge list to adj list 
        adj = {}
        for u,v in edges:
            
            adj[u] = adj.get(u,[])
            adj[v] = adj.get(v,[])

            adj[u].append(v)
            adj[v].append(u)


        visited = set()
        
        def dfs(node):

            if node in visited:
                return

            
            visited.add(node)

            for nei in adj[node]:
                dfs(nei)
        

        ### Important ###
        # There can be nodes with no edges
        # So those remaining edges are components in themselves
        components = n - len(adj) 
        for node in adj:
            if node not in visited:
                dfs(node)
                components += 1
        
        return components
        '''


        ### DSU - Unionfind ###
        # Just normal union find
        # Time: O(V+(E∗α(V)))
        # Space: O(V)
        
        components = n
        parents = {}
        ranks = {}

        for i in range(n):
            parents[i] = i
            ranks[i] = 0
        print(parents)
        
        
        def find(node):

            cur = node

            while cur != parents[cur]:
            
                # Optimization 
                parents[cur] = parents[parents[cur]]
                # Move up
                cur = parents[cur]
        
            return cur


        def union(n1, n2):
            
            nonlocal components
            root_n1, root_n2 = find(n1), find(n2)

            if root_n1 == root_n2:
                return True
        
            if ranks[root_n1] > ranks[root_n2]:
                parents[root_n2] = root_n1
            elif ranks[root_n1] < ranks[root_n2]:
                parents[root_n1] = root_n2
            else:
                parents[root_n2] = root_n1
                ranks[root_n1] += 1
        
            components -= 1

            return False

        for u,v in edges:
            union(u,v)
        
        return components
