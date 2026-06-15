##### Idea ########
# Trie is prefix tree, the node shape of children dictionary and word boolean variable to store
# if character is word end.
# There is a dummy root node i.e. TrieNode whose children store the first charcters
# Trie vs array vs set 
# Complexity comparison :
# Exact search -> Set >> Trie >> Array  
# Prefix search -> Trie >> Set == Array 
# Space complexity -> Array == Set == Trie unless data given in array/set/trie and have to convert
# Insert -
# Time: O(n), where n = length of word
# Space: O(n) worst case new nodes for one insert
# Total Trie Space: O(t), where t = total TrieNodes created
# Search -
# Time: O(n)
# Aux Space: O(1)
# Prefix Search -
# Time: O(n), where n = length of prefix
# Aux Space: O(1)

class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):

        ### Dummy root node
        self.root = TrieNode()

    def insert(self, word: str) -> None:

        ### Idea :
        ## The idea is to put every character in a word into the previous characters children, starting with root 
        # If the character is last, set cur word true
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.word = True



    def search(self, word: str) -> bool:

        ### Idea 
        ## Search from charaacter to character if found and also word is true at end then return true

        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.word 
        

    def startsWith(self, prefix: str) -> bool:
        
        ### Idea 
        ## Search from character to character if found then return true

        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        
        
        