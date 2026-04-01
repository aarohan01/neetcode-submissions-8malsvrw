class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = []
        ### Bruteforce ###
        for i in range(len(temperatures)):
            flag = 0
            for j in range(i+1,len(temperatures)):

                if temperatures[j] > temperatures[i]:
                    res.append(j-i)
                    flag = 1
                    break
            if flag == 0:
                res.append(0)

        return res


        