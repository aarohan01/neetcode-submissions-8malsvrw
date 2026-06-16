class TrieNode:

    def __init__(self):

        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:

        cur =  self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]

        # Last letter    
        cur.word = True

    def search(self, word: str) -> bool:

        
        def dfs(node,windex):

            cur = node

            for idx in range(windex, len(word)):
                ch = word[idx]

                # Case 1 : If character is '.'
                # Search next index i.e next ch on all the cur children's children
                # So cur children will be nodes
                if ch == '.':
                
                    # values as we want the node associated with letter 
                    # or can use cur.children[]
                    for c in cur.children.values():
                        
                        # Skip the current index
                        # If any return true return true
                        if dfs(c, idx+1):
                            return True
                    
                    # If all return False
                    return False
                
                # Case 2 : If character is not '.'
                # Match it in children if it matches keep going else return false
                else:

                    if ch in cur.children:
                        cur = cur.children[ch]
                    else:
                        return False 
            return cur.word
        
        return dfs(self.root, 0)


            

    

        
        
