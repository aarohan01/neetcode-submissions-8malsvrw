class Solution:
    def isValid(self, s: str) -> bool:

        ### Bruteforce ###
        # Repeatedly remove bracket pairs from the string 

        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        
        if not s:
            return True 
        return False
            








        