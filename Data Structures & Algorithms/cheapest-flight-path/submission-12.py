import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        ### Dijkstra - BFS with heap and res dict ###


        # Adj list from edges
        # n is given, directed

        adj = {node:[] for node in range(n)}
        for u, v, cost in flights:
            adj[u].append((cost,v))
        
        print(adj)

        # Heap 
        minheap = []
        # Res stores the stops not cost
        res = {}

        # No mark on enque 
        # while we use cost to pop from heap we don't add to res if the stops are greater
        # We allow rewrite of res if stops are less
        # (cost,stops,node)
        # The other important thing is res stores stops not cost
        heapq.heappush(minheap, (0,0,src))

        while minheap:

            cost, stops, node = heapq.heappop(minheap)

            if node == dst:
                return cost

            if stops > k : 
                continue
            
            # If the answer in res is with lower stops
            if node in res and res[node] <= stops:
                continue

            res[node] = stops
            
        
            for nei_cost, nei in adj[node]:
                # No check for already in res
                if nei not in res or res[nei] > (stops+1):
                    heapq.heappush(minheap, ( cost+nei_cost, stops + 1,nei))
        
        print(res)
        return -1


