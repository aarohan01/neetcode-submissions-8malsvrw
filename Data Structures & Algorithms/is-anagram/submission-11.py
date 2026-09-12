class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        ### Bruteforce ###
        # nlogn 
        # s + t
        #return sorted(s) == sorted(t)

        def hashtable(string):

            arr = [0]*26
            for i in string:
                arr[ord(i)-ord('a')] += 1
            return arr

        return hashtable(s) == hashtable(t)