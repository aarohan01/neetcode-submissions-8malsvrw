class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #Bruteforce 
        #Loop through and find the combination 
        #Since two loops , O(n^2) and O(n)


        #Solution 1
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