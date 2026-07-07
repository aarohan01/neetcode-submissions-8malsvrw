from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        

        ### BFS single source ###
        # We can form a graph, it will be undirected and unweighted
        # So shortest path on unweighted unidirected graph is BFS 
        # The most important part is making the graph 
        # The length of all words given are fixed i.e. all words same length
        # So naive way is to compare each word to every other word 
        # Time: O(n^2 * m) where n is the number of words and m is length of words, so creating graph is n^2*m
        # and BFS is (V+E) -> n + n^2 thus creation dominates
        # Space: O(n^2)  -> O(V+E) -> n + n^2 -> n^2
        # The only reason this is not optimal is a trick.
        # Since word length is bounded by 10 and words are bounded by 5000 (Given)
        # Instead of constructing graph by looping word we can loop differently.
        '''
        def one_diff(w1, w2):

            diff = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff += 1
                
                if diff > 1:
                    return False
            
            return True

        ### Edge case where endWord itself is not present ###
        if endWord not in wordList:
            return 0

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
        
        # Default return 
        return 0
                
        '''

        #### BFS single source - optimal ###
        # Using a trick since length is <= 10 which is much smaller.
        # And all words are fixed length
        # So we can use pattern matching
        # Time: O(m^2*n)
        # Space: O(n*m^2) -> createing the adj

        ### Edge case where endWord itself is not present ###
        if endWord not in wordList:
            return 0

        # Note start word may not be in list so check seperately 
        if beginWord not in wordList:
            wordList.append(beginWord)

        n = len(wordList)
        adj = {}

        # Createing pattern of every word based on length in adj 
        # n*m*m -> second m is for slicing 
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i+1:]

                adj[pattern] = adj.get(pattern, [])
                ### IMPORTANT ###
                if word not in adj[pattern]:
                    adj[pattern].append(word)
            

        #print(adj)

        ### BFS ###
        ## The main difference will be searching based on length and pattern
        # for every word the neighbors are all its pattern neigbors excluding itself
        # m*m*n -> for length of a word * slice it * explore neigbhor ( n coz one visit each node)
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

                for i in range(len(node)):
                    pattern = node[:i] + '*' + node[i+1:]

                    for nei in adj[pattern]:
                        if nei not in visited:

                            # Mark on enque
                            queue.append(nei)
                            visited.add(nei)
                    
                    adj[pattern] = []

            dist += 1
        
        # Default return 
        return 0
        
