from collections import deque

BLANK = 0
WALL = 1
VIRUS = 2

n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

copy_grid = [
    row[:]
    for row in grid
]

visited = [
    [False] * m
    for _ in range(n)
]

picked = []
blank_pos = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == BLANK]
k = len(blank_pos)
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
ans = 0


def init():
    for i in range(n):
        for j in range(m):
            grid[i][j] = copy_grid[i][j]
            visited[i][j] = False


def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < m


def simulate():
    global ans

    # init
    init()

    # set walls
    for row, col in picked:
        grid[row][col] = WALL

    # BFS from Virus
    for i in range(n):
        for j in range(m):
            if grid[i][j] == VIRUS and not visited[i][j]:
                bfs(i, j)

    # Count safe area
    ans = max(ans, len([
        (i, j)
        for i in range(n)
        for j in range(m)
        if grid[i][j] == BLANK
    ]))


def bfs(i, j):
    queue = deque()
    visited[i][j] = True
    queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if in_range(nx, ny) and grid[nx][ny] == BLANK and not visited[nx][ny]:
                visited[nx][ny] = True
                grid[nx][ny] = 2
                queue.append((nx, ny))


def pick_wall(idx, cnt):
    global ans
    if cnt == 3:
        simulate()
        return
    if idx == k:
        return

    for i in range(idx, k):
        picked.append(blank_pos[i])
        pick_wall(i + 1, cnt + 1)
        picked.pop()


pick_wall(0, 0)
print(ans)
