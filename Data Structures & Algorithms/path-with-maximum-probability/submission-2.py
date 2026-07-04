import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        

        ### Bruteforce - DFS explore all path and then calulate ###





        ### Dijsktra - MaxHeap + Stop when target ###
        ## Undirected Edges and Weighted graph
        ## Source given and target also given so we can early stop 
        # Probability is multiplication
        # We need MAX prop not MIN 


        # adj list
        # n given and undirected
        adj = {node:[] for node in range(n)}
        '''
        for e in range(len(edges)):

            adj[edges[e][0]].append((succProb[e], edges[e][1]))
            adj[edges[e][1]].append((succProb[e], edges[e][0]))

        print(adj)
        '''

        for e, prob in zip(edges,succProb):

            adj[e[0]].append((prob, e[1]))
            adj[e[1]].append((prob, e[0]))

        print(adj)




        ### modified BFS + maxheap and res dict ###

        maxHeap = []

        # Start probability will be 1 not 0 as its multiplication
        # maxHeap hence -1
        heapq.heappush(maxHeap, (1, start_node))

        res = {}

        while maxHeap:

            prob, node = heapq.heappop(maxHeap)

            if node in res:
                continue

            res[node] = abs(prob)

            if node == end_node:
                return res[node]

            for nprob, nei in adj[node]:

                if nei not in res:
                    total_prob = abs(prob * nprob)
                    heapq.heappush(maxHeap, (-total_prob, nei))

        
        return 0

        



