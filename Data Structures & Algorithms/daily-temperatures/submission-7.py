class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        
        ### Bruteforce ###
        # Time : O(n)
        # Space : O(1)
        '''
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):

                if temperatures[j] > temperatures[i]:
                    res[i] = j-i
                    break
        return res
        '''

        ### Stack ###
        # Next greater hence stack is best option 
        # Its running difference - If a higher temp is detected that means for whatever is in the stack currently we can 
        # count days instead of calculaling for each individually , until stack is in desc order we just move on the for loop 
        # appending elements, when detected we pop and store diff and continue the for loop for remaining elements that means 
        # all elements are visited only once.
        ## Better to use tuple monotonic stack for clarity ##
        '''
        res = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                    j = stack.pop()
                    res[j] = i - j
                    
            stack.append(i)
        return res
        '''
        ## Same using tuple ##
        res = [0]*len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                    val, idx = stack.pop()
                    res[idx] = i - idx
                    
            stack.append((t,i))
        return res




        