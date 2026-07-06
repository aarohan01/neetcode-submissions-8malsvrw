import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        


        #### Kruskal's ####


        #### Prim's Heap ###
        # Edge list not given thus need to calculate and make adj list.
        # Dijkstra - BFS with priority queue, res dict pop only one time 
        # Prims - BFS with pirority queue, visited set pop only one time - main difference is cost 
        # Prims uses the cost from current node Dijkstra uses cost from source node.
        # Also since source node is not given start from any node.
        # Prims also works on Adj List similart to Dijkstra
        # Time: O(V + ElogE) -> Creating adj is V + E and the Prims is ElogE because the height of tree is logE
        # Space: O(V + E) -> Adj list
        
        # calculate and add to Adj List
        # n given, undirected
        n = len(points)
        adj = {node:[] for node in range(n)}
        for i in range(n):
            for j in range(n):
                if i != j:
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