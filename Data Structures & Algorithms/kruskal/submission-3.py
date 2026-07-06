class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:

        #### Kruskal's ####
        # Kruskal needs edge list 
        # Kruskal -> sorted edgelist and then use DSU on it to check cycle 
        # Just keep adding mincost edge list while checking cycle with DSU
        # Time: O(V^2logV) -> O(V^2logV^2+ alphaE)
        # Space: O(V^2)  -> O(E)

        ### DSU ###

        components = n
        parents = {i:i for i in range(n)}
        ranks = {i:0 for i in range(n)}
        
        def find(node):

            cur = node
            while cur != parents[cur]:
                ### Optimization ###
                parents[cur] =  parents[parents[cur]]
                cur = parents[cur]
            
            return cur

        
        def union(node1, node2):

            nonlocal components
            parent1, parent2 = find(node1), find(node2)

            ### Cycle ###
            if parent1 == parent2:
                return True

            ### Optimization ###
            if ranks[parent1] > ranks[parent2]:
                parents[parent2] = parent1
            elif ranks[parent1] < ranks[parent2]:
                parents[parent1] = parent2
            else:
                parents[parent2] = parent1
                ranks[parent1] += 1

            components -= 1
            return False


        ### Kruskal's ###
        ## Edges 
        ### Sorting ###
        #sedges = [[cost, u, v] for u, v, cost in edges]  
        #sedges.sort()
        edges.sort(key=lambda x: x[2])


        ### MST ###
        minimum_sum = 0
        MST = []

        #for  cost, u, v in sedges:
        for u, v, cost in edges:
            if not union(u,v):
                minimum_sum += cost
                MST.append([u,v])

        ### Component will be 0 (empty graph) or greater than 1 (disconnected graph)
        if components != 1:
            return -1
        print(MST)
        return minimum_sum