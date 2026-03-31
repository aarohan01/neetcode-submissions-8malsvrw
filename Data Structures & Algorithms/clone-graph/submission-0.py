from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        ### Solution ###
        # The Question only gives representation of graph, the input is going to be only a single starting node
        # Given : Undirected conncected connected graph -> all nodes reachable from all nodes
        # no duplicate nodes
        # INPUT - First Node in Adj List 
        # OUTPUT - First Node of our graph  
        # VALUES - same as it index(starting from 1)

        # Either of BFS and DFS can be used
        # Using BFS + HashMap ( to maintain )
        # We maintain a hashmap to note which nodes are already created.

        
        ## Edge case - No node;
        if not node:
            return None
        
        ## Setup ## 
        # To maintain mapping
        nodeMap = {}
        # BFS 
        queue = deque()
        new = Node(node.val)
        nodeMap[node] = new
        # OG node to explore
        queue.append(node)
    
        

        print(f'First Node - Nodes: {nodeMap} Queue: {queue}')

        while len(queue) > 0:

                # No need to maintain level so skipping the loop 

                curr = queue.popleft()

                # We do not know the target, so we skip that check 

                # We loop through neighbors and check if they are already created
                for n in curr.neighbors:
                    if n not in nodeMap:
                        
                        # Create if not created
                        
                        print(f'Creating : {n.val}')
                        nodeMap[n] = Node(n.val)

                        # Explore OG node children
                        queue.append(n)
                    
                    # We created children but didn't add to neigbors of new node
                    nodeMap[curr].neighbors.append(nodeMap[n])



                        

        return nodeMap[node]






