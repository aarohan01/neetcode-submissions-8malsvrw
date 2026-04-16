class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:



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

        ### Bruteforce Improved - Using set and not storing fleets ###
        '''
        data = [(position[i], speed[i], (target - position[i])/speed[i] ) for i in range(len(position))]
        data.sort(reverse=True)
        #print(data)
        visited = set()
        fleets = 0
        for i in range(len(data)):
            if data[i] in visited:
                continue
            for j in range(i, len(data)):
                
                if data[j] not in visited:

                    if data[j][2] <= data[i][2]:
                        visited.add(data[j])

            fleets += 1
        #print(fleets)
        return fleets
        '''

        ### Iteration - Optimized  ###
        ## Important Observation :
        # The biggest observation is --> Even if some car has faster speed it cannot get ahead 
        # of a car that is already is position ahead of it.
        # So its meaningless to compare to all the cars ahead of it.
        # So starting from closest to target if car takes less time then still it is part of fleet
        # if it takes more then it is part of new fleet and subsequent cars can be compared to this car
        # Ex : [4,1,0,7] [2,2,1,1] -> sorted [7,4,1,0] [1,2,2,1]
        # So 7 starts a fleet =1, time req for 4 == 7 (3) part of same fleet = 1 remains
        # Then come 1, time req > prev fleet thus new fleet, fleet = 2, fleet time updated
        # Then comes 0, time req > prev fleet thus new fleet, fleet = 3, fleet time updated

        # Acceptable sorting but trying zip
        #data = [(position[i], speed[i]) for i in range(len(position))]
        #data.sort(reverse=True)
        data = sorted(zip(position,speed), reverse=True)
        
        fleet = 0
        fleet_time = None
        for i in range(len(data)):
            
            # First car
            '''
            if i == 0:
                fleet += 1
                fleet_time = (target - data[i][0])/data[i][1]
                continue
            '''
            
            time = (target - data[i][0])/data[i][1]
            if not fleet_time or time > fleet_time:
                fleet += 1
                fleet_time = time 
        
        return fleet

    ### Stack ###
    ## Iteration is better to understand and also as optimized so prefer iteration
    # Maintain the fleet leaders time in stack

    #data = zip(position,speed)
    #data.sort(reverse=True)


            
                    



        

