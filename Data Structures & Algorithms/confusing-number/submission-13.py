class Solution:
    def confusingNumber(self, n: int) -> bool:


        ### Build inverse in a list ###
        number = n
        res = []
    
        while n:

            digit = n % 10
            if digit in [2,3,4,5,7]:
                return False
            
            elif digit in [0,1,8]:
                res.append(str(digit))
            
            elif digit == 6:
                res.append('9')
            else:
                res.append('6')

            n = n // 10


        if not res or int(''.join(res)) == number:
            return False

        return True


        ### Hashmap + Direct inverse ###
        number = n
        inverse = 0
        digit_map = {0:0,1:1,6:9,8:8,9:6}


        while n:

            digit = n % 10
            if digit not in digit_map:
                return False
            else:
                inverse = inverse*10 + digit_map[digit]

            n = n // 10

        if number == inverse:
            return False

        return True