class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])
        l, h = 0, M*N - 1

        while l <= h:
            mid = (l + h) // 2

            m = mid // N
            n = mid % N

            if matrix[m][n] == target:
                return True
            elif matrix[m][n] > target:
                h = mid - 1
            else:
                l = mid + 1
        
        return False