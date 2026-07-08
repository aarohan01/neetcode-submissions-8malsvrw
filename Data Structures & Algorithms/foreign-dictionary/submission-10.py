class Solution:
    def foreignDictionary(self, words: List[str]) -> str:



        # Given : The strings are sorted in lex order in alien language
        # Sorting condition:
        # 1. If a is prefix of b then it should appear before it -> can check 
        # 2. If a appears before b, then first letter not same in a is smaller -> have to assume that in alien lang letter in 
        # a is smaller (not in our language)
        # detect cycle and give order as well so Topological Sort (Directed)

        def getedge(w1, w2):
            
            p1, p2 = 0, 0
            while p1 < len(w1) and p2 < len(w2):

                if w1[p1] == w2[p2]:
                    p1 += 1
                    p2 += 1
                    continue
                
                return [w1[p1], w2[p2]]

            if p1 != len(w1):
                return False
            


        edges = []
        for i in range(len(words)-1):
            
            edge = getedge(words[i], words[i+1])
            if edge == False:
                return ""
            elif edge == None:
                continue
            else:
                edges.append(edge)


        
        print(edges)

        ### Tops Sort - by order so will need reverse ###
        ## 3-color dfs + res stored (backtracking & return aggregation )

        # Adj List
        # Directed n not given
        adj = {c: [] for w in words for c in w}
        for src, dst in edges:
            adj[src] = adj.get(src,[])
            adj[dst] = adj.get(dst,[])

            adj[src].append(dst)
        
        print(adj)

        visiting = set()
        done = set()
        res = []

        ## Boolean return aggregation 
        def dfs(node):
            
            # Cycle
            if node in visiting:
                return True

            if node in done:
                return False

            visiting.add(node)

            for nei in adj[node]:

                if dfs(nei):
                    return True

            
            visiting.remove(node)
            done.add(node)
            res.append(node)

            return False

        
        # Can be disconnected
        for node in adj:
            if node not in done:
                if dfs(node):
                    return ""
        
        return ''.join(res[::-1])



            
            
            


