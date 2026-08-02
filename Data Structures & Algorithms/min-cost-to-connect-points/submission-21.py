import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        


        #### Kruskal's ####
        # Kruskal needs edge list 
        # Kruskal -> sorted edgelist and then use DSU on it to check cycle 
        # Just keep adding mincost edge list while checking cycle with DSU
        # Time: O(V^2logV) -> O(V^2logV^2+ alphaE)
        # Space: O(V^2)  -> O(E)
        '''
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
        ##### REMEMBER AN UNDIRECTED EDGE REPRESENTS BOTH WAYS unlike adj list #####
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([dist,i,j])
        
        ### Sorting ###
        edges.sort()


        ### MST ###
        minimum_sum = 0
        MST = []

        for cost, u, v in edges:
            if not union(u,v):
                minimum_sum += cost
                MST.append([u,v])

        ### Component will be 0 (empty graph) or greater than 1 (disconnected graph)
        if components != 1:
            return -1
        print(MST)
        return minimum_sum

        '''
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


        ### Prim's Array ###
        # In a dense graph compliexity of Prim's array version is better V^2 
        # Dense : E > V upto V^2 
        ## IMPORTANT : This problem is not just dense since we can connect any point to any point
        ## this is a completely connected graph.
        ## In that case we don't even need adj list since we can visit any node from any node thus no need of 
        ## list of neighbors present in adj, just check from n.
        ### This is very similar to Bellman Ford Algo 
        ## From a node at every round we find distance to all its neighbors and do this n times
        ## In this particular problem every point is every point's neigbor in other problems we do adj list
        # **We set the min distance in the distance array every round i.e. current distance and new distance min**
        # In bellman we are adding edges in here we are adding nodes thus for n rounds
        # Time: o(n^2)
        # Space: O(n)
        
        n = len(points)
        # Setup
        distances = [float('inf')]*n
        distances[0] = 0
        visited = set()

        # result
        minimum_distance = 0
        # Visiting every node
        while len(visited) < n:

            # Dummy values
            node = None
            dist = float('inf')

            # Find next node that cost's less than inf
            for i in range(n):
                if i not in visited and distances[i] < dist:
                    node = i
                    dist = distances[i]

            # Disconnected i.e. can't connect every point
            if node == None:
                return -1

            # Visit 
            visited.add(node)
            minimum_distance += dist

            # Explore neigbors
            for nei in range(n):
                if nei not in visited:
                    nei_dist = abs(points[node][0] - points[nei][0]) + abs(points[node][1] - points[nei][1])
                    distances[nei] = min(distances[nei],nei_dist)
                    #print(nei, distances,visited)

        
        return minimum_distance

