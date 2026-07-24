class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:





        ### Intervals - sort and compare start and ends ###
        # O(nlogn)
        # O(1) aux
        
        intervals.sort()
        merged = [intervals[0]]
        
        for i in range(1,len(intervals)):
            
            prev = merged[-1]
            cur = intervals[i]
            if cur[0] <= prev[1]:
                start = prev[0]
                end = max(prev[1],cur[1])
                #print(start,end)
                ### Note last set not append ###
                merged[-1] = [start,end]
            else:
                merged.append(cur)

        return merged
        