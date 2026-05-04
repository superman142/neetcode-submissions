class Node:

    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if not c in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        
        curr.end = True
        

    def search(self, word: str) -> bool:
        
        def dfs(i, node):
            if i == len(word):
                return node.end
            
            if word[i] == ".":
                for v in node.children.values():
                    if dfs(i + 1, v):
                        return True
            elif word[i] in node.children:
                return dfs(i + 1, node.children[word[i]])

            return False

        return dfs(0, self.root)

        

