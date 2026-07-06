import heapq
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:

        # Dijkstra - BFS with priority queue, res dict  pop only one time 
        # Prims - BFS with pirority queue with visited set pop only one time - main difference is cost 
        # Prims uses the cost from current node Dijkstra uses cost from source node.
        # Also since source node is not given start from any node.
        # Prims also works on Adj List similart to Dijkstra
        
        # Edge list to Adj List
        # n given, undirected
        adj = {node:[] for node in range(n)}
        for src, dst, cost in edges:
            adj[src].append((cost,dst))
            adj[dst].append((cost,src))

        print(adj)



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







        