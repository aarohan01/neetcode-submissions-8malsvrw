class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        

        ### DFS normal coverage multicell ###
        ## Source not given can be disconnected - multicell
        ## Need to visit once every node - normal coverage

        
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

        components = n - len(adj) 
        for node in adj:
            if node not in visited:
                dfs(node)
                components += 1
        
        return components



        ### DSU - Unionfind ###
