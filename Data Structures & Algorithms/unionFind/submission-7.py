### Idea ###
## Structure - for every node store parent for every node store rank
# Initially every node has parent None and rank/height 0
# Number of components is thus n

## Find - Idea is to find the root of a component i.e. parent 
# If no parent then itself should be parent, thus in structure by default we set the node itself as parent 
# Otherwise we can set None and do that in find

## Union - Merging of components - merging is just linking a parent to another parent (parent is itself if no parent)
# Given is nodes we find parents and merege the parent with lower rank into parent with higher rank
# This keep the tree height small - draw and check 
# If rank is same merge any way like say mere node 2 to node 1 but increment rank of what becomes parent since it goes higher
# Reduce components if union successful

## Cycle Detection - undirected 
# If can't union because already same component then cycle
# Ex :  1 - 2 - 3   4 - 5  components created, now  we get edge 1 - 4
class UnionFind:
    
    def __init__(self, n: int):

        self.num_components = n
        self.parent = {}
        self.rank = {}

        ### Initial parent and height/rank ##
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0
        

    def find(self, x: int) -> int:
        
        ## Without optimization ##
        cur = self.parent[x]
        while cur != self.parent[cur]:
	        # Optimization parent make parent 
            self.parent[x] = self.parent[self.parent[x]]
            cur = self.parent[cur]
        
        return cur

    def isSameComponent(self, x: int, y: int) -> bool:
        par_x = self.find(x)
        par_y = self.find(y)

        ### Already in same component cycle (undirected graph) / Cannot merge ###
        if par_x == par_y:
            return True
        
        return False
        

    def union(self, x: int, y: int) -> bool:

        par_x = self.find(x)
        par_y = self.find(y)

        ### Already in same component cycle (undirected graph) / Cannot merge ###
        if par_x == par_y:
            return False

        if self.rank[par_x] > self.rank[par_y]:
            self.parent[par_y] = par_x
        elif self.rank[par_y] > self.rank[par_x]:
            self.parent[par_x] = par_y
        else:
            self.parent[par_y] = par_x
            self.rank[par_x] += 1
        
        self.num_components -= 1
        return True
        

    def getNumComponents(self) -> int:
        
        ### When we union we set node's parent's parent ###
        ## So self.parent only contains parent of each node not the roots of component ##
        # We can gets roots using find#

        #components = len({ self.find(x) for x in range(self.n) })
        # OR 
        #components = len({ self.find(x) for x in self.parent})
        #return components



        ### WE CAN ALSO MAINTAIN THE COMPONENT NUMBERS WHILE UNION ###
        ## Start from every node as num_components in constructor and decrease as we union ###
        return self.num_components
