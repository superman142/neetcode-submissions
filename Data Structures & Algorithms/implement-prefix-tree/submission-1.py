class Node:
    def __init__(self):
        self.letters = {}
        self.end = False


class PrefixTree:

    def __init__(self):
        self.start = Node()
        

    def insert(self, word: str) -> None:
        curr = self.start

        for c in word:
            if c not in curr.letters:
                curr.letters[c] = Node()
            curr = curr.letters[c]
        
        curr.end = True


    def search(self, word: str) -> bool:
        curr = self.start

        for c in word:
            if c not in curr.letters:
                return False
            
            curr = curr.letters[c]
        
        return curr.end


    def startsWith(self, prefix: str) -> bool:
        curr = self.start

        for c in prefix:
            if c not in curr.letters:
                return False
            
            curr = curr.letters[c]
        
        return True

        
        