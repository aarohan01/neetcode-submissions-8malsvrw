import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        


        #### Kruskal's ####
        # Kruskal needs edge list 
        # Kruskal -> sorted edgelist and then use DSU on it to check cycle 
        # 

        ### DSU ###

        n = len(points)
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
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([dist,i,j])
                edges.append([dist,j,i])
        
        ### Sorting ###
        edges.sort()


        ### MST ###
        minimum_sum = 0
        MST = []

        for cost, u, v in edges:
            if not union(u,v):
                minimum_sum += cost
                MST.append([u,v])

        return minimum_sum








        #### Prim's Heap ###
        # Edge list not given thus need to calculate and make adj list.
        # Dijkstra - BFS with priority queue, res dict pop only one time 
        # Prims - BFS with pirority queue, visited set pop only one time - main difference is cost 
        # Prims uses the cost from current node Dijkstra uses cost from source node.
        # Also since source node is not given start from any node.
        # Prims also works on Adj List similart to Dijkstra
        # Time: O(V^2logV)  ->  V^2 (calculating adj list) + ElogE  - >  V^2 + V^2 log V^2 -> 2V^2 log V
        # Space: O(V^2) ->  V + E  -> V + V^2 -> V^2
        '''
        # calculate and add to Adj List
        # n given, undirected , careful as we are already looping
        n = len(points)
        adj = {node:[] for node in range(n)}
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append((dist,j))
                adj[j].append((dist,i))

        #print(adj)



        # Heap for the next node to select and visited to track cycle
        # MST to store result
        # No mark on enque just put in minHeap
        minHeap = [] 
        visited = set()
        minimum_dist = 0

        # Cost to reach 1st Node is 0, and any node can be selected selecting 0
        heapq.heappush(minHeap, (0, 0))


        while minHeap:

            cost, node = heapq.heappop(minHeap)

            # Guard : don't explore already visited nodes
            if node in visited:
                continue

            # visited node
            visited.add(node)
            minimum_dist += cost

            # Add neigbhors to the heap if not already visited based on the immediate cost.
            # So next node poppoed will be the min edge from current node not the source node.
            for nei_cost, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (nei_cost, nei))

        
        if len(visited) != len(adj):
            return -1
        return minimum_dist
        '''