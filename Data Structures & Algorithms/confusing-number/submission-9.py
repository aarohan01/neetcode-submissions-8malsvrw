class Solution:
    def confusingNumber(self, n: int) -> bool:

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