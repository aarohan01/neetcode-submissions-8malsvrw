from collections import deque
class Graph:

    
    def __init__(self):
        
        ### Adjacency List ###
        self.adj = {}
            

    def addEdge(self, src: int, dst: int) -> None:
        
        if src not in self.adj:
            self.adj[src] = []
        self.adj[src].append(dst)
        print(f'{self.adj}')


    def removeEdge(self, src: int, dst: int) -> bool:
        
        if src not in self.adj:
            self.adj[src] = []
            print(f'{self.adj}')
            return False

        if dst in self.adj[src]:
            self.adj[src].remove(dst)
            print(f'{self.adj}')
            return True

        print(f'{self.adj}')
        return False


    def hasPath(self, src: int, dst: int) -> bool:

        ### BFS ###
        # Since one path, better to do BFS as easy to implement

        def bfs(node, target, adj):

            # We traverse level by level
            # We use a queue add the source then loop through the queue to  visit children.
            # If we have already reached the target return the level
            # Else loop through and  check the adj list of the node, 
            # The only condition is :
            # 1. already visited
            # 2. blocked if given
            # Else add to queue and visited.
            # Increment the level outside   


            # Setup 
            queue = deque()
            visited = set()
            queue.append(node)
            visited.add(node)

            # Originally BFS is used to get length but here we are returning bool 
            #length = 0

            while len(queue) > 0:
                for i in range(len(queue)):
                    curr = queue.popleft()
                    if curr == target:
                        print(f'Exixts {curr}:{target}')
                        return True

                    for n in adj.get(curr, []):

                        # Conditions
                        if n not in visited:
                            queue.append(n)
                            visited.add(n)

            print(f'Not exixts {curr}:{target}')     
            return False

        return bfs(src, dst, self.adj)


        '''
        ### DFS ### 
        # DFS counts the number of paths

        s, d = src, dst
        visited  = set ()

        def dfs(adj, s, d, visited):

            # Base case 1 : Failure 
            # Failure in case of grid was multiple conditions, but in adj list we don't have to check bounds
            if d not in adj[s] :
                return 0
            
            if s == d:
                return 1

            count =  0
            visited.add(node)
            
            for d in adj[node]:
                count += dfs(adj, s, d, visited)

            visited.remove(node)    

            return count 


        

        if dfs(self.adj, s, d, visited) > 0:
            return True
        return False
        '''