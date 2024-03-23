def copy_matrix(matrix):
    return matrix

def input_matrix(rows):
    matrix = []

    for _ in range(rows):
        matrix.append(list(map(int, input().split())))

    return matrix

def mult_matrix_to_matrix(matrix_a, matrix_b):
    matrix_r = [[0] * len(matrix_a) for _ in range(len(matrix_a))]

    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_a[0])):
                matrix_r[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return matrix_r

def print_matrix(matrix):
    for i in matrix:
        print(*i)
    return

if __name__ == '__main__':
    rows = int(input())
    matrix_a = input_matrix(rows)
    matrix_r = copy_matrix(matrix_a)


    for _ in range(int(input()) - 1):
        matrix_r = mult_matrix_to_matrix(matrix_r, matrix_a)

    print_matrix(matrix_r)
