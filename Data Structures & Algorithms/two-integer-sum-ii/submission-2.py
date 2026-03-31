class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #Bruteforce 
        #Loop through and find the combination 
        #Since two loops , O(n^2) and O(n)

        '''
        #Solution 1 # Works but missed condition that solution needs to be space O(1)
        #Similar to two sum, just add the conditons of index1 !=  index2 and 
        #index1 < index2 -> already the case in twosum solution of hashmap

        prevMap = {}

        for i,num in enumerate(numbers):
            diff = target - num
            if diff in prevMap :
                if prevMap[diff] != i :
                    return [prevMap[diff]+1,i+1]   
            else:
                prevMap[num] = i     
        '''

        ### Solution 2 ###
        #After seeing hint 3 - using two pointer to take advantage of array already being sorted.

        l = 0
        r = len(numbers) - 1

        while l < r :

            if numbers[l] + numbers[r] > target :
                r -= 1
            elif numbers[l] + numbers[r] < target :
                l += 1
            else : 
                return [l+1,r+1]
        
        return []




