class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class WordTree:
    def __init__(self):
        self.root = Node()
    
    def add(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])

        ret = set()
        wordTree = WordTree()

        for word in words:
            wordTree.add(word)

        seen = set()

        def dfs(r, c, node, word):
            if (min(r, c) < 0 or
                r >= ROWS or
                c >= COLS or
                (r, c) in seen or
                board[r][c] not in node.children):
                return
            
            nextNode = node.children[board[r][c]]
            newWord = word + board[r][c]

            if nextNode.end:
                ret.add(newWord)

            seen.add((r, c))
            dfs(r - 1, c, nextNode, newWord)
            dfs(r + 1, c, nextNode, newWord)
            dfs(r, c - 1, nextNode, newWord)
            dfs(r, c + 1, nextNode, newWord)
            seen.remove((r, c))


        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, wordTree.root, "")
        
        return list(ret)

        
                

