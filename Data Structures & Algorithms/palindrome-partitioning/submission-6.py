class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        '''
        def palCheck(string):

            L,R = 0, len(string)-1

            while L < R:
                if string[L] != string[R]:
                    print(string)
                    return False
                L += 1
                R -= 1
            
            return True

        res, partition = [], []
        def dfs(index):
            

            # Base Case : Failure
            ### Important here to only check the last term added in path and not scan everything
            ## Because the previous terms are already checked for.
            if partition and not palCheck(partition[-1]):
                return 

            # Base Case : Success
            if index == len(s):
                res.append(partition.copy())


            for end in range(index+1,len(s)+1):
                
                partition.append(s[index:end])
                dfs(end)
                partition.pop()
            

        dfs(0)
        return res
        '''
            

        ### Backtracking - optimal ###
        ## The solution above is almost optimal since we only check for the last appended element
        # But instead we can check it before recursion call to prune
        
        res, partition = [], []
        def dfs(index):
            

            # Base Case : Failure
            ### Important here to only check the last term added in path and not scan everything
            ## Because the previous terms are already checked for.
            # Base Case : Success
            if index == len(s):
                res.append(partition.copy())


            for end in range(index+1,len(s)+1):
                
                piece = s[index:end]
                ### Here piece is always going to be atleast one letter because how we wrote for look
                if palCheck(piece):

                    partition.append(piece)
                    dfs(end)
                    partition.pop()


        def palCheck(string):

            L,R = 0, len(string)-1

            while L < R:
                if string[L] != string[R]:
                    #print(string)
                    return False
                L += 1
                R -= 1
            
            return True

        dfs(0)
        return res

        