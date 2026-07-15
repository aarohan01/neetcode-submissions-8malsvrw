class Solution:
    def partition(self, s: str) -> List[List[str]]:
        

        def palCheck(string):

            L,R = 0, len(string)-1

            while L <= R:
                if string[L] != string[R]:
                    print(string)
                    return False
                L += 1
                R -= 1
            
            return True

        res, partition = [], []
        def dfs(index):
            

            # Base Case : Failure
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

            


        