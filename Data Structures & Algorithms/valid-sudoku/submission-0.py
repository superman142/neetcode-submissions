class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # horizontal
        M = len(board)
        N = len(board[0])

        for i in range(M):
            curr = set()
            for j in range(N):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] not in curr:
                    curr.add(board[i][j])
                else: 
                    return False
        

        # vertical
        for j in range(N):
            curr = set()
            for i in range(M):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] not in curr:
                    curr.add(board[i][j])
                else:
                    return False
        
        boxSets = [[set() for i in range(3)] for j in range(3)]

        for i in range(M):
            for j in range(N):
                if board[i][j] == ".":
                    continue
                
                if board[i][j] not in boxSets[i//3][j//3]:
                    boxSets[i//3][j//3].add(board[i][j])
                else:
                    return False
        
        return True




