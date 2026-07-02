class UnionFind:

    def __init__(self,n):
        
        self.components = n
        self.parents = {}
        self.ranks = {}

        for i in range(1,n+1):
            self.parents[i] = i
            self.ranks[i] = 0
        print(self.parents)
    
    def find(self, node):

        cur = self.parents[node]

        while cur != self.parents[cur]:
            
            # Optimization 
            self.parents[cur] = self.parents[self.parents[cur]]
            # Move up
            cur = self.parents[cur]
        
        return cur


    def union(self, n1, n2):

        root_n1, root_n2 = self.find(n1), self.find(n2)

        if root_n1 == root_n2:
            return True
        
        if self.ranks[root_n1] > self.ranks[root_n2]:
            self.parents[root_n2] = root_n1
        elif self.ranks[root_n1] < self.ranks[root_n2]:
            self.parents[root_n1] = root_n2
        else:
            self.parents[root_n2] = root_n1
            self.ranks[root_n1] += 1
        
        self.components -= 1

        return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        

        ### DFS normal coverage multicell + skip parent cycle detection ###

        ### THIS CODE CORRECTLY DETECTS CYCLE AND GIVES THE EDGE ###
        ## But the issue is that it gives the edge in order of nodes ##
        # The question expects the edge that causes cycle to be in the order or the edge list #
        # Example : Edgelist : [[1,2],[1,3],[2,3]] 
        # According to this if we use adj list to construct graph 
        # We will go from 1 - 2 - 3 - 1 and detect cycle and return [1,3] as cycle edge 
        # But the question expects [2,3] because if we used edge list it would be 1-2 then 1-3 and 2-3 causing cycle
        # So in reality any edge removal is sufficient but answer is expected in order of edge list
        ##############################################################


        '''
        ## Since undirected and where ever there is cycle its extra edge.
        ## Only one extra edge


        # Converting edge list to adj list for DFS
        adj = {}

        for x,y in edges:
            
            adj[x] = adj.get(x,[])
            adj[y] = adj.get(y,[])

            # Undirected thus both ways
            adj[x].append(y)
            adj[y].append(x)

        print(adj)

        visited = set()
        cycle_nodes = []
        def dfs(node,parent):
            
            # Cycle
            if node in visited:
                cycle_nodes.append(node)
                cycle_nodes.append(parent)
                return True


            visited.add(node)

            for nei in adj[node]:

                ### Skip parent ###
                if nei == parent:
                    continue
                
                if dfs(nei, node):
                    return True

            return False

        
        for node in adj:
            print(node)
            if node not in visited:
                if dfs(node,None):
                    return cycle_nodes
        '''

        ### Union Find cycle detection ###
        ## Edge list given and we want edge that causes cycle - Union Find 


        # Create UnionFind DS
        n = len(edges)
        uf = UnionFind(n)

        for u,v in edges:
            print(u,v)
            if uf.union(u,v):
                return [u,v]
        

            




            