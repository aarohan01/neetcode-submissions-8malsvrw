import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        

        ### Dijkstra ###
        ## Weighted Directed Graph given
        ## Why Dij and not MST :
        # 1. Directed Graphs
        # 2. At once simultaneously we can travel multiple paths, in the given example if 1 to 4 was cost 1 
        # at time unit 1 we reach both node 2 and node 4.
        # Then another unit we reach all nodes

        # Minimum time to get to all nodes is max time of all times
        # Basically if we calculate time taken to each node and then find out the max of it
        # Since min time depends on the node that takes max time.



        # Adj list from edge list
        # n given and directed
        adj = {node:[] for node in range(1,n+1)}
        for src, dst, time in times:
            
            adj[src].append((time,dst))
        
        print(adj)


        ### modified BFS + minheap and res ###
        minHeap = []

        heapq.heappush(minHeap, ((0,k)))
        res = {}
        maxcost = 0
        while minHeap:

            cost, node = heapq.heappop(minHeap)

            if node in res:
                continue

            res[node] = cost
            maxcost = max(maxcost, cost)

            for ncost, nei in adj[node]:

                if nei not in res:
                    heapq.heappush(minHeap, (cost + ncost, nei))

        '''
        for node in adj:
            if node not in res:
                return -1
        '''
        if len(adj) != len(res):
            return -1

        return maxcost

    