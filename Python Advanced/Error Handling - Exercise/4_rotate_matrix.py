class MatrixContentError(Exception):
    pass

def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()

mtrx = []

valid_numbers= '1234567890'


while True:
    line = input().split()
    for c in line:
        if not c.isdigit():
            raise MatrixContentError("The matrix must consist of only integers")
    if not line:
        break
    mtrx.append(line)


class MatrixSizeError(Exception):
    pass


for row in mtrx:
    if len(row) != len(mtrx):
        raise MatrixSizeError("The size of the matrix is not a perfect square")

rotate_matrix(mtrx)

for row in mtrx:
    print(*row, sep=' ')
