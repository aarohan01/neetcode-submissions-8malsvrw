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

        ### Trie DFS + Backtracking for '.' wildcard ###
        # Case 1 Normal char:
        # Check if char exists in cur.children, move cur if yes else return False
        
        # Case 2 Dot '.':
        # Dot can be any child, so try dfs(child, next index) for every child node
        # MOST IMPORTANT: if any child dfs returns True, return True to parent immediately
        # If child returns False, control comes back to parent and parent tries next child
        # If all children fail, return False
        
        # Base case:
        # When pattern ends, return cur.word
        # cur.word checks exact word ending, not just prefix path existing
        
        # Time: addWord O(n), search O(n) without dots, worst O(26^d * n) with dots but since dots limited to 2
        # its O(n)
        # Space: addword O(t) -> all nodes created in add word, O(n) for search.
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
                        # THIS IS THE MOST IMPORTANT STEP 
                        # THIS PASES TO THE PARENT EVERYTHING EVERYTIME
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
            
            # Base case when word ends since we want the pattern matching to end on word end
            # If it was just this pattern exists in path ther would have return True instead
            return cur.word
        
        return dfs(self.root, 0)


            

    

        
        
