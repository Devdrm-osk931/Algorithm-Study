#BOJ_Class4_17070_Gold5

n = int(input())

# 갈 수 있는 위치/벽: 0/1
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 0: 가로 1: 세로 2: 대각선
cnt = [
    [
        [0] * n
        for _ in range(n)
    ]
    for _ in range(3)
]

for idx in range(1, n):
    if grid[0][idx] == 1:
        break
    cnt[0][0][idx] = 1

# for floor in cnt:
#     for row in floor:
#         for elem in row:
#             print(elem, end=' ')
#         print()
#     print("=============")
# print("========================================")

for r in range(1, n):
    for c in range(2, n):
        # 대각선으로 현재 위치에 들어오기 위해선 현재 위치, 위 옆이 모두 빈칸이어야 한다
        if not grid[r][c] and not grid[r-1][c] and not grid[r][c-1]:
            cnt[2][r][c] = cnt[0][r-1][c-1] + cnt[1][r-1][c-1] + cnt[2][r-1][c-1]

        # 가로 또는 세로 방향으로 현재 위치에 들어오기 위해서는 해당 칸이 빈칸이어야 한다
        if not grid[r][c]:
            # 대각 -> 가로 & 가로 -> 가로
            cnt[0][r][c] += cnt[0][r][c-1] + cnt[2][r][c-1]

            # 대각 -> 세로 & 세로 -> 세로
            cnt[1][r][c] += cnt[1][r-1][c] + cnt[2][r-1][c]

# for floor in cnt:
#     for row in floor:
#         for elem in row:
#             print(elem, end=' ')
#         print()
#     print("================")

# 답은 마지막 위치에 대한 모든 방향을 더한 값
print(cnt[0][n - 1][n - 1] + cnt[1][n - 1][n - 1] + cnt[2][n - 1][n - 1])