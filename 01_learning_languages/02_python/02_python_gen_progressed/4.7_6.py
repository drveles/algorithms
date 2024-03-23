def input_matrix(rows):
    matrix = []

    for _ in range(rows):
        matrix.append(list(map(int, input().split())))

    return matrix

def sum_matrix(matrix_a, matrix_b):
    matrix_r = [[0] * len(matrix_a[0]) for _ in range(len(matrix_a))]

    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[0])):
                matrix_r[i][j] += matrix_a[i][j] +  matrix_b[i][j]

    return matrix_r

def print_matrix(matrix):
    for i in matrix:
        print(*i)
    return

if __name__ == '__main__':

    rows, cols = list(map(int, input().split()))
    matrix_a = input_matrix(rows)
    input()
    matrix_b = input_matrix(rows)

    print_matrix(sum_matrix(matrix_a, matrix_b))

