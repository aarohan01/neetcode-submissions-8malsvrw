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
        # If the character is last, set word true
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
        ## Search from charaacter to character if found and also word is true at end then return true

        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
        
        
        