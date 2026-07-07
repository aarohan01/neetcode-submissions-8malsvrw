class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        
        ### DSU - need to check if cycle and one component ###
        # A valid tree will have no cycle and only one component #
        # Undirected + edges given -> DSU
        # Time: O(V + E*(alphaV)) -> V comes from parent and ranks creation rest is DSU
        # Space: O(V) -> parents and ranks


        ### Edge Case ###
        ## A tree will never have edges other than 1 less if it is lesser -> disconnected, more 
        # then its a cycle
        if len(edges) != n-1 :
            return False

        components = n
        parents = {node:node for node in range(n)}
        ranks = {node:0  for node in range(n)}


        def find(node):

            cur = node
            while cur != parents[cur]:
                parents[cur] =  parents[parents[cur]]
                cur = parents[cur]
            
            return cur

        
        def union(node1, node2):

            nonlocal components 

            parent1, parent2 = find(node1), find(node2)

            ### Cycle ###
            if parent1 == parent2:
                return True

            
            if ranks[parent1] > ranks[parent2]:
                parents[parent2] = parent1
            elif ranks[parent1] < ranks[parent2]:
                parents[parent1] = parent2
            else:
                parents[parent2] = parent1
                ranks[parent1] += 1
            
            components -= 1
            return False

        for u,v in edges:
            ### Cycle ###
            if union(u,v):
                return False
        
        ### Disconnected ###
        if components != 1:
            return False
        
        ### Valid Tree ###
        return True

        

