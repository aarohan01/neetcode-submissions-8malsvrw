from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        

        ### BFS single source ###
        # We can form a graph, it will be undirected and unweighted
        # So shortest path on unweighted unidirected graph is BFS 
        # The most important part is making the graph 
        # The length of all words given are fixed i.e. all words same length
        # So naive way is to compare each word to every other word 


        def one_diff(w1, w2):

            diff = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff += 1
                
                if diff > 1:
                    return False
            
            return True

        # Note start word may not be in list so check seperately 
        if beginWord not in wordList:
            wordList.append(beginWord)

        n = len(wordList)
        adj = {word:[] for word in wordList}

        for i in range(n):
            for j in range(i+1,n):
                if one_diff(wordList[i], wordList[j]):
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        

        #print(adj)

        ### BFS ###
        queue = deque()
        visited = set()

        queue.append(beginWord)
        # Mark on enque
        visited.add(beginWord)

        # Need to give nodes not edges
        dist = 1
        while queue:

            for q in range(len(queue)):

                node = queue.popleft()

                # Break condition 
                if node == endWord:
                    return dist


                for nei in adj[node]:
                    if nei not in visited:

                        # Mark on enque
                        queue.append(nei)
                        visited.add(nei)

            dist += 1
        
        return 0
                

