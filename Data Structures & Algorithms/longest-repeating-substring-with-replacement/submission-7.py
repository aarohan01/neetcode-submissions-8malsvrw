class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        ### Bruteforce ###
        # The idea isn't about the characters but can be framed as longest subarray with repeating characters, 
        # but with k repeats allowed.
        # For each element calculate subarray that has repeating characters till non-repeating character appears,
        # two choices, if k not 0 then allow counting else break

        ### Problem : It won't look into past letters, example k=1 s = AABBB, answer should be 4 but its 3
        # coz it doesn't check thus we can reverse. To solv

        ### But this is a very weird solution a GREEDY SOLUTION ###
        # Time : O(n^2)
        # Space : O(1)
        '''
        maxlen = 0

        for L in range(len(s)):
            curlen = 0
            c = k
            seen = s[L]
            print(L)
            for R in range(L, len(s)):
                
                if s[R] == seen[-1]:
                    curlen += 1
                    seen = s[R]
                    print(f'R - {R} seen: {seen} s[R] - {s[R]} - curlen {curlen}')
                elif c > 0:
                    curlen += 1
                    c -= 1
                    #seen.append(seen[-1])
                    print(f'R - {R} seen: {seen} s[R] - {s[R]} - curlen {curlen}')
                else:
                    break

                maxlen = max(curlen,maxlen)
            
            if c > 0:
                print('reverse')
                for R in range(L-1,-1,-1):
                    if s[R] == seen[-1]:
                        curlen += 1
                        seen = s[R]
                        print(f'R - {R} seen: {seen} s[R] - {s[R]} - curlen {curlen}')
                    elif c > 0:
                        curlen += 1
                        c -= 1
                        #seen.append(seen[-1])
                        print(f'R - {R} seen: {seen} s[R] - {s[R]} - curlen {curlen}')
                    else:
                        break

                maxlen = max(curlen,maxlen)

                
        return maxlen
        '''
        
        ### Bruteforce ###
        # For each letter, check a window where consecutive same elements and update maxlen, allow k non-consecutive.
        # But do it based on freq or characters, maintain a freq map for the window and also allow k non-consecutive based on
        # most freq element in the window
        maxlen = 0
        for L in range(len(s)):
            freq = [0] * 26
            for R in range(L, len(s)):
                idx = ord(s[R]) - ord('A')
                freq[idx] += 1
	    
                maxfreq = max(freq)
                length = R - L + 1
	    
                if length - maxfreq <= k:
                    maxlen = max(maxlen, length)
	    
        return maxlen



            

