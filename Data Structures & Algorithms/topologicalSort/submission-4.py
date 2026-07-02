class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:


        # Convert to Adj List
        # n is given 
        adj = {i:[] for i in range(n)}
        for src, dst in edges:
            adj[src].append(dst)        

        #print(adj)

        visiting = set()
        done = set()
        res = []

        def dfs(node):

            # Cycle 
            if node in visiting:
                return True
            
            # No cycle just done
            if node in done:
                return False

            visiting.add(node)

            for nei in adj[node]:

                if dfs(nei):
                    return True


            
            visiting.remove(node)
            done.add(node)
            res.append(node)

            return False

        for node in adj:
            if node not in visiting:
                if dfs(node):
                    return []
        
        return res[::-1]

