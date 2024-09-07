class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        len_mat = len(mat)

        for i in range(len_mat):
            for j in range(len_mat):
                if i == j or i + j == len_mat - 1:
                    result += mat[i][j]

        return result


# OK, 56%, 43%
