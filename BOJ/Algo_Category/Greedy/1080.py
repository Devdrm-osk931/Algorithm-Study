# BOJ_1080_행렬

n, m = tuple(map(int, input().split()))

A = [
    list(map(int, list(input())))
    for _ in range(n)
]

B = [
    list(map(int, list(input())))
    for _ in range(n)
]


# 0 -> 1/1 -> 0 matrix[row][col] ~ matrix[row + 2][col + 2]
def flip(matrix, r, c):
    for row in range(r, r + 3):
        for col in range(c, c + 3):
            matrix[row][col] ^= 1

def print_matrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=' ')
        print()

count = 0
for row in range(n - 2):
    for col in range(m - 2):
        if A[row][col] != B[row][col]:
            flip(A, row, col)
            count += 1

print(-1 if A != B else count)