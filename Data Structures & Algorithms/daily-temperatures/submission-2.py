class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0]*len(temperatures)
        ### Bruteforce ###
        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):

                if temperatures[j] > temperatures[i]:
                    res[i] = j-i
                    break

        return res


        