class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals = {}

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i - j in diagonals:
                    diagonals[i - j].append(mat[i][j])
                else:
                    diagonals[i - j] = [
                        mat[i][j],
                    ]

        for diagonal in diagonals.values():
            diagonal.sort(reverse=True)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = diagonals[i - j].pop()

        return mat


# OK, 65%, 50%
