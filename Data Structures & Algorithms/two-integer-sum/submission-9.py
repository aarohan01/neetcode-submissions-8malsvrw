class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        #Bruteforce solution :
        #Check all the combinations and give output
        #two loop hence O(n^2) and O(n)

        #Solution 
        #Use a hashmap - Loop through the array and check if target - the current is 
        #in the hashmap, if not append the current term and its indice.
        #If yes then give both indices.


        hashMap = {}
        for i,num in enumerate(nums):

            index1 = hashMap.get(target-num,-1)
            if index1 != -1:
                return [index1,i]
            else :
                hashMap[num] = i
        
        