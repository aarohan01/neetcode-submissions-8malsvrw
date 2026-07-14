class Solution:
    def letterCombinations(self, digits: str) -> List[str]:


        ### Bruteforce - Backtracking as subsets no dupes ###
        # Generating all subsets but selecting only with size k, where k is given as 4 and n is given as 7 (2 to 9)
        # No reuse, dupes so subset dupes pattern for bruteforce 
        # Time: For time complexity n is actually digits which is max 4 and from each branch O(n * (4C1)^n)
        # The max is going to be 4c1*4C1*4C1*4C1 -> here the 4 is for max letters per digit(3 or 4) and max amount of digits is 4 which we say n
        # copy n letters as well so n * 4^n
        # Space: O(k) -> at a time only k elements stored
        '''
        res, combination = [], []
        hashmap = {
            '2':['a','b','c'], 
            '3':['d','e','f'], 
            '4':['g','h','i'], 
            '5':['j','k','l'], 
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
             }

        #letters = []
        #for s in digits:
            #letters += hashmap[s]

        #print(letters)

        def dfs(i,k):

            # Base case 1 :  success 
            if len(combination) == k:
                res.append(combination.copy())
                return 

            # Base case 2 : failure
            # len(combination) > k not needed coz k always hits unlike sum
            if i > n:
                return 
            
            # Choice 1:
            # Take and advance
            for letter in hashmap[i]:
                combination.append(letter)
                dfs(i+1)

            # Choice 2:
            # Skip and advance
            combination.pop()
            dfs(i+1)
        
        dfs(digits[0], len()
        #return res
        '''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res, strings = [], []
        def backtrack(i):

            # Base Case : Success 
            if len(strings) == len(digits):
                res.append(strings.copy())

                return

            for d in digitToChar[digits[i]]:
                for c in d:
                    strings.append(c)
                    backtrack(i+1)
                    #print(strings)
                    strings.pop()


        if digits:
            backtrack(0)

        return [''.join(s) for s in res ]
        