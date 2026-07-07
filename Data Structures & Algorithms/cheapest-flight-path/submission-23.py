import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        ### Dijkstra - BFS with heap and res dict ###
        ### Not Optimal - since we give one thing that is the adv of dijkstra not revisiting nodes
        # Modified Dijkstra, where we store results based on different criteria than cost
        # Allow it to overwrite because its not the cheapest cost but based on stops
        '''
        # Adj list from edges
        # n is given, directed

        adj = {node:[] for node in range(n)}
        for u, v, cost in flights:
            adj[u].append((cost,v))
        
        #print(adj)

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
                # No check for already in res (check is optional)
                # If not in res or the answer in res is higher we push 
                if nei not in res or res[nei] > (stops+1):
                    heapq.heappush(minheap, ( cost+nei_cost, stops + 1,nei))
        
        #print(res)
        return -1
        '''
        

        ### Bellman Ford ###
        distances = [float('inf')]*n
        distances[src] = 0

        ### We have to have only k stops 
        # A -> B -> C : n=3   2 edges -> normal case
        # A -> B -> C : k=1   2 edges allowed -> thus k+1  


        for _ in range(k+1):
            temp = distances.copy()
            for s, d , w in flights:
                #print(distances)
        
                if distances[s] == float('inf'):
                    continue
                
                temp[d] = min(temp[d], distances[s] + w)


            distances = temp
        
        return distances[dst] if distances[dst] != float('inf') else -1
                

