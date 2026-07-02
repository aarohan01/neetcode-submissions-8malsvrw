import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:

        
        # Adj List from edge list 
        # n is given + directed graph
        adj = {node:[] for node in range(n) }
        for s, d, cost in edges:
            
            # We already created all the empty lists for all nodes beforehand since n was given
            adj[s].append((cost,d))

        print(adj)

        # Heap i.e. Priority Queue and visit set
        # BFS -> mark on enqueue
        minHeap = []
        res = {}

        heapq.heappush(minHeap,(0,src))
        res[src] = 0
        

        print(res,'XXX')


        while minHeap:

            cost, node = heapq.heappop(minHeap)

            if node not in res:
                #print(node)
                res[node] = cost 

            for nei_cost, nei in adj[node]:
                if nei not in res:
                    heapq.heappush(minHeap,(cost + nei_cost, nei))
        
        
        for node in adj:
            if node not in res:
                res[node] = -1

        return res


        

        

        