class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        if not s:
            return 0
        

        i = len(s)-1

        while s[i] == ' ':
            i -= 1
        print(i)

        length = 0
        for j in range(i,-1,-1):

            if s[j] != ' ':
                length += 1
            else:
                break

        return length

