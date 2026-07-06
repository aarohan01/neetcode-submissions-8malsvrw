class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        

        ### DFS ###

        # Edge list to Adj List
        # n not given and directed
        adj = {}
        ### Sort ahead, since order of nodes don't matter neighbors matter 
        tickets.sort(reverse=True)
        for src, dst in tickets:

            adj[src] = adj.get(src, [])
            adj[dst] = adj.get(dst, [])

            adj[src].append(dst)

        # sort the neighbors lexicographically 
        # But reverse so we can pop from end
        #for node in adj:
            #adj[node].sort(reverse=True)

        print(adj)

        # Start with 'JFK' always 
        res = []

        def dfs(node):
    
            while adj[node]:
                nei = adj[node].pop()
                dfs(nei)

            res.append(node)

        dfs('JFK')
        return res[::-1]

