class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        changed = True

        while changed:
            changed = False
            i = 0

            while i <= len(s) - k:
                # Check if next k chars are same
                if s[i:i+k] == s[i] * k:
                    s = s[:i] + s[i+k:]
                    changed = True
                    break  # restart scan from beginning
                
                i += 1

        return s


            
    
                    
        

                
        

            
