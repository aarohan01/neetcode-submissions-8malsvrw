import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        
        ### Dijkstra - BFS single source with result dictionary and minheap, no visit set ###
        # Time adj list : O(V+E)
        # Time Dijkstra : O(ElogE)
        # Time: O(V + ElogE)
        # Space: O(V+E)


        # Adj List from edge list 
        # n is given + directed graph
        adj = {node:[] for node in range(n) }
        for s, d, cost in edges:
            
            # We already created all the empty lists for all nodes beforehand since n was given
            adj[s].append((cost,d))

        #print(adj)

        # Heap i.e. Priority Queue and visit set
        minHeap = []
        heapq.heappush(minHeap,(0,src))
        
        # Result dictionary storing mincost to each node from source
        res = {}
        while minHeap:

            cost, node = heapq.heappop(minHeap)

            # Skip checking anything if node is already in result (as it will have min cost due to minheap)
            if node in res:
                continue

            # Else set the cost and explore neighbor to find out next min cost neighbor
            res[node] = cost 

            # Put all the nighbors that are not visited to minheap to then get min cost 
            for nei_cost, nei in adj[node]:
                if nei not in res:
                    heapq.heappush(minHeap,(cost + nei_cost, nei))
        
        
        # Set -1 for nodes that can't be reached from source i.e. disconnected.
        for node in adj:
            if node not in res:
                res[node] = -1

        return res


        

        

        