class Solution:
    def numDecodings(self, s: str) -> int:
        

        #choices + base cases 
        # choose either one digit or 2 digit 
        # Base cases success -> string end -> 1 
        # Base cases failure -> invalid string -> 0
        # 
        '''
        valid = set([str(i) for i in range(1,27)])
        def decode(si, ei):

            if si < len(s) and ei >= len(s):
                return 0
            if s[si:ei+1] not in valid:
                return 0
            if ei ==len(s)-1:
                return 1

            return decode(ei+1,ei+1) + decode(ei+1,ei+2)

        return decode(0,0) + decode(0,1)
        '''


        ### Better Recursion ###
        ### Why is above bad idea ? the chunk is irrelevant in next call every call we
        # check current or current + next as chunk.
        # One index check if invalid  i is 0 or i = 2 and i+1 > 6 
        # we start at index 0 and check index i and index i+1
        # similar to count in exploreall path i.e. backtracking but just don't backtrack

        ## Choice is either one digit or two from start index
        # Base cases -> success check if i reaches end 
        # Base case -> failure -> index string is 0
        # Else  -> two choices either advance 1 index or advance 2 index based on condition
        
        dp = [None]*(len(s)+1)

        def dfs(i):

            if dp[i] is not None:
                return dp[i]

            if i == len(s):
                return 1
            if s[i] == '0':
                return 0

            res = dfs(i + 1)
            if i+1 < len(s):
                if (s[i] == '1' or
                   (s[i] == '2' and s[i + 1] < '7')):
                    res += dfs(i + 2)
            
            dp[i] = res
            return dp[i]

        return dfs(0)