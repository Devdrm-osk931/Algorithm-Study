# BOJ 2638
# 치즈
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

temp = [
    [0 for _ in range(m)]
    for _ in range(n)
]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def done():
    for i in range(n):
        for j in range(m):
            if grid[i][j]:
                return False
    return True


def init_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False
            temp[i][j] = 0


# 치즈에 의해 둘러쌓여 있지 않은 영역을 표시한다
def dfs(start):
    x, y = start
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not visited[nx][ny] and not grid[nx][ny]:
            visited[nx][ny] = True
            dfs((nx, ny))


def melt():
    for i in range(n):
        for j in range(m):
            if not grid[i][j]:
                continue
            # 치즈 주변에 치즈 외부에 있는 빈칸의 갯수를 찾는다
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                if in_range(nx, ny) and visited[nx][ny] and not grid[nx][ny]:
                    temp[i][j] += 1

    for i in range(n):
        for j in range(m):
            if temp[i][j] >= 2:
                grid[i][j] = 0


def simulate():
    answer = 0
    while not done():
        answer += 1
        init_visited()

        # 치즈와 분리되어 있는 영역을 처리한다
        visited[0][0] = True
        dfs((0, 0))

        melt()
    print(answer)


simulate()