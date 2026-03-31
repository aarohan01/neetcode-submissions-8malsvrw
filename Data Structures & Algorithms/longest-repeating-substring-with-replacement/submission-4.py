class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        ### Bruteforce ###
        # The idea isn't about the characters but can be framed as longest subarray with repeating characters, 
        # but with k repeats allowed.
        # For each element calculate subarray that has repeating characters till non-repeating character appears,
        # two choices, if k not 0 then allow counting else break

        ### Problem : It won't look into past letters, example k=1 s = AABBB, answer should be 4 but its 3
        # coz it doesn't check 
        maxlen = 0

        for L in range(len(s)):
            curlen = 1
            c = k
            seen = [s[L]]
            print(L)
            for R in range(L+1, len(s)):
                
                if s[R] == seen[-1]:
                    curlen += 1
                    seen.append(s[R])
                    print(f'R - {R} seen: {seen} s[R] - {s[R]} - curlen {curlen}')
                elif c > 0:
                    curlen += 1
                    c -= 1
                    seen.append(seen[-1])
                    print(f'R - {R} seen: {seen} s[R] - {s[R]} - curlen {curlen}')
                else:
                    break

                maxlen = max(curlen,maxlen)
            
            if c > 0:
                print('reverse')
                for R in range(L-1,-1,-1):
                    if s[R] == seen[-1]:
                        curlen += 1
                        seen.append(s[R])
                        print(f'R - {R} seen: {seen} s[R] - {s[R]} - curlen {curlen}')
                    elif c > 0:
                        curlen += 1
                        c -= 1
                        seen.append(seen[-1])
                        print(f'R - {R} seen: {seen} s[R] - {s[R]} - curlen {curlen}')
                    else:
                        break

                maxlen = max(curlen,maxlen)

                
        return maxlen
            
        