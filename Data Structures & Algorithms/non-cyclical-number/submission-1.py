class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        ### Bruteforce ###
        hashset = set()
        
        while n != 1:
            total = 0
            while n:
                total += (n % 10)**2
                n = n // 10
            
            print(total)
            if total in hashset:
                return False
            hashset.add(total)
            n = total
        return True
                
