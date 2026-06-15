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

        #print(self.root.children)
        
        ### Similar to for loop combination backtrackinng ###
        def searchWord(node, windex):
            
            cur = node


            for w in range(windex,len(word)):

                if word[w] != '.':

                    if word[w] not in cur.children :
                        return False
                    else:
                        cur = cur.children[word[w]]

                else:

                    for c in cur.children:

                        if searchWord(cur.children[c],w+1):
                            return True
                    
                    return False
            return cur.word
        return searchWord(self.root, 0)

            

    

        
        
