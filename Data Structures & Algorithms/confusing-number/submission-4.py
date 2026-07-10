class Solution:
    def confusingNumber(self, n: int) -> bool:


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