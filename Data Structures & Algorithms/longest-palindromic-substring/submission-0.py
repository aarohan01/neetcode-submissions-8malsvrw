class Solution:
    def longestPalindrome(self, s: str) -> str:


        ### Substring -> like subarray contiguous and ordered
        # palindrome when reverse is equal to itself


        ### 
        # for every single letter check if its palindrome if yes then expand to left and right
        # while exapanding check if it goes past

        reslen = 0
        residx = None
        for i in range(len(s)):
            start, end = i,i
            while start >= 0 and end < len(s):
                chunk = s[start:end+1]
                if chunk == chunk[::-1]:
                    if end - start + 1 > reslen:
                        reslen = end - start + 1
                        residx = (start,end+1)
                start -= 1 
                end += 1

        for i in range(len(s)):
            start, end = i,i+1
            while start >= 0 and end < len(s):
                chunk = s[start:end+1]
                if chunk == chunk[::-1]:
                    if end - start + 1 > reslen:
                        reslen = end - start + 1 
                        residx = (start,end+1)
                start -= 1 
                end += 1

        print(reslen)
        print(residx)
        

            


        return s[residx[0]:residx[1]]