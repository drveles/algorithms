class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals = {}

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i - j not in diagonals:
                    diagonals[i - j] = [mat[i][j]]
                else:
                    heapq.heappush(diagonals[i - j], mat[i][j])

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = heapq.heappop(diagonals[i - j])

        return mat
