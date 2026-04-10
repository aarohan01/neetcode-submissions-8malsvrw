class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        ### Bruteforce ###
        '''
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
        '''

        ### Floyd's fast and slow pointers ###
        # If we draw the results of each addition and read the question "non-cyclical"
        # That means if we detect a cycle in this linked list it is False
        # If instead we find value 1 then true

        ### Returns next number in the linked list i.e. next number after n ###
        def nextNumber(n:int) -> int:
        
            total = 0
            while n:
                total += (n % 10)**2
                n = n // 10
            return total
        
        
        
        curfast, curslow = nextNumber(nextNumber(n)), nextNumber(n)
        print(curfast,curslow)

        while curfast != 1 or curslow != 1:

            if curfast == curslow:
                return False
            
            curfast, curslow = nextNumber(nextNumber(curfast)), nextNumber(curslow)
        
        return True
            
            



                
