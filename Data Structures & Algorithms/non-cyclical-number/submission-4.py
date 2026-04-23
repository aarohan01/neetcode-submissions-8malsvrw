class Solution:
    def isHappy(self, n: int) -> bool:
        
        
        ### Bruteforce ###
        # Using a hashset to see if number appeared already if yes return False
        # If at any stage number becomes 1 return True
        # Time: O(logn)
        # Space: O(logn)
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
        # Time : O(logn)
        # Space : O(1)

        ### Returns next number in the linked list i.e. next number after n ###
        def nextNumber(n:int) -> int:
        
            total = 0
            while n:
                total += (n % 10)**2
                n = n // 10
            return total
        
        
        # For number n let curslow be next num and curfast is next to next
        # If curfast or curslow is 1 at any stage its non-cyclical return true
        # If curfast and curslow meet anywhere there is a cycle thus return false
        curfast, curslow = n, n
        print(curfast,curslow)
        while curfast != 1 and nextNumber(nextNumber(curfast)) != 1:
            
            curfast, curslow = nextNumber(nextNumber(curfast)), nextNumber(curslow)

            if curfast == curslow:
                print(curfast,curslow)
                return False
            
            
        
        return True
            
            



                
