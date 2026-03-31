class Solution:
    def scoreOfString(self, s: str) -> int:
        
        ### Bruteforce ###
        score = 0
        for i in range(len(s)-1):
            #print(f'{s[i+1]} - {ord(s[i+1])}  {s[i]} - {ord(s[i])} sub {(ord(s[i+1]) - ord(s[i]))}')
            score  += abs(ord(s[i+1]) - ord(s[i]))
        return score

