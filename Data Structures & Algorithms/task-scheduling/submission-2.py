class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


        ### Bruteforce ###
        ## The most important intuition is that, 
        # In order for time to be least we need to do the most frequent task first i.e. prioritise it.
        # So that the gap or idle time is lesser


        count = len(tasks)
        hashmap = {}
        for i in tasks:
            hashmap[i] = hashmap.get(i,0)+1
        print(hashmap)
        
        freqtable = [0]*len(hashmap)
        for idx,val in enumerate(hashmap.values()):
            freqtable[idx] = val
        
        print(freqtable)

        ### Main intuition ###
        time = 0
        while count > 0:
            freqtable.sort(reverse=True)
            cycles = n + 1
            i = 0
            while i < len(freqtable) and cycles > 0:

                if freqtable[i] == 0:
                    i += 1
                    continue
                    
                freqtable[i] -= 1
                cycles -= 1
                count -= 1
                time += 1
                i += 1
            ## Remaining cycles ##
            # Apart from the last loop
            if count > 0:
                time += cycles 
        return time
