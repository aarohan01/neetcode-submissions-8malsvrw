class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        ### Bruteforce ###
        '''
        visited = []
        fleets = []
        for i in range(len(position)):
            if position[i] in visited:
                continue
            curfleet = [position[i]]
            for j in range(len(position)):

                if i != j and position[j] not in visited and position[j] < position[i]:

                    curtime = (target - position[i])/speed[i]
                    othertime = (target - position[j])/speed[j]

                    if othertime <= curtime :
                        print(f'J:{position[j]} ot:{othertime} I:{position[i]} ct:{curtime}')
                        curfleet.append(position[j])
            fleets.append(curfleet)
            visited += curfleet
        
        print(fleets)
        return len(fleets)
        '''

        # If for a car if its time taken is less than time taken by someone in position higher
        # then they belong to same fleet.
        '''
        data = [(position[i], speed[i]) for i in range(len(position))]
        data.sort(reverse=True)
        #print(data)
        visited = []
        fleets = []
        for i in range(len(data)):
            if data[i] in visited:
                continue
            curfleet = [data[i]]
            for j in range(i+1, len(data)):
                
                if data[j] not in visited:
                    itime = (target - data[i][0])/data[i][1]
                    jtime = (target - data[j][0])/data[j][1]

                    if jtime <= itime:
                        curfleet.append(data[j])

            fleets.append(curfleet)
            visited += curfleet
        #print(fleets)
        return len(fleets)
        '''

        ### Bruteforce Improved ###
        data = [(position[i], speed[i]) for i in range(len(position))]
        data.sort(reverse=True)
        #print(data)
        visited = []
        fleets = 0
        for i in range(len(data)):
            if data[i] in visited:
                continue
            #curfleet = [data[i]]
            curfleet = []
            for j in range(i, len(data)):
                
                if data[j] not in visited:
                    itime = (target - data[i][0])/data[i][1]
                    jtime = (target - data[j][0])/data[j][1]

                    if jtime <= itime:
                        curfleet.append(data[j])

            fleets += 1
            visited += curfleet
        #print(fleets)
        return fleets




                    



        

