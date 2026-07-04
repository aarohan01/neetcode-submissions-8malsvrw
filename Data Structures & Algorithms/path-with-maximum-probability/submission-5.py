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
        heapq.heappush(maxHeap, (-1, start_node))

        res = {}

        # Note : Only heap has negative, res and adj has positive prob so be careful with signs
        # Push negative to heap
        while maxHeap:

            prob, node = heapq.heappop(maxHeap)

            ## Heap Stored negative, but res we need positive ##
            # Flipping once 
            prob = abs(prob)

            if node in res:
                continue

            res[node] = prob

            if node == end_node:
                return res[node]

            for nprob, nei in adj[node]:

                if nei not in res:
                    # Prob is positive and nprob is also positive (from adj)
                    # Answer will be pos, just push
                    total_prob = -(prob * nprob)
                    #print(total_prob)
                    heapq.heappush(maxHeap, (total_prob, nei))

        
        return 0

        



