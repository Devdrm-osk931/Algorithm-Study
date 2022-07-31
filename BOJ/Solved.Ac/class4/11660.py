#BOJ_11660_Silver1_구간합구하기

import sys
input = sys.stdin.readline

n, m = tuple(map(int, input().split()))

values = [
    list(map(int, input().split()))
    for _ in range(n)
]

# dp[row][col] --> (1, 1) ~ (row, col)
dp = [
    [0 for _ in range(n + 1)]
    for _ in range(n + 1)
]

# 행 별로 더하고 열 별로 더해도 같은 결과를 도출할 수 있음
for row in range(n):
    for col in range(n):
        dp[row + 1][col + 1] = dp[row + 1][col] + dp[row][col + 1] - dp[row][col] + values[row][col]

for _ in range(m):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    print(dp[x2][y2] + dp[x1 - 1][y1 - 1] - dp[x1 - 1][y2] - dp[x2][y1 - 1])