#BOJ_1932_정수 삼각형

import sys
si = sys.stdin.readline

n = int(si())

values = [
    list(map(int, si().split()))
    for _ in range(n)
]

# print("OG")
# for row in values:
#     for elem in row:
#         print(elem, end = ' ')
#     print()

for row in range(1, n):
    for col in range(row + 1):
        if col == 0:
            values[row][col] = values[row - 1][col] + values[row][col]
        elif col == row:
            values[row][col] = values[row - 1][col - 1] + values[row][col]
        else:
            values[row][col] = max(values[row - 1][col - 1], values[row - 1][col]) + values[row][col]

# print()
# print("DP")
# for row in values:
#     for elem in row:
#         print(elem, end = ' ')
#     print()

print(max(values[n - 1]))