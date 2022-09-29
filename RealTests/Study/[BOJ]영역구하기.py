# BOJ 영역구하기 실버1
# Samsung
import heapq, sys
sys.setrecursionlimit(10 ** 9)

m, n, k = tuple(map(int, input().split()))

wall = [
    [False for _ in range(m)]
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

while True:
    try:
        a, b, c, d = tuple(map(int, input().split()))
        for row in range(a, c):
            for col in range(b, d):
                wall[row][col] = True
    except:
        break


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def dfs(x, y, cnt):
    visited[x][y] = True

    for dx, dy in zip(dxs, dys):
        nx , ny = x + dx, y + dy
        if in_range(nx, ny) and not wall[nx][ny] and not visited[nx][ny]:
            cnt = dfs(nx, ny, cnt + 1)

    return cnt


answer = []
cnt = 0
for row in range(n):
    for col in range(m):
        if not visited[row][col] and not wall[row][col]:
            area = dfs(row, col, 1)
            cnt += 1
            heapq.heappush(answer, area)

print(cnt)
while answer:
    print(heapq.heappop(answer), end=' ')