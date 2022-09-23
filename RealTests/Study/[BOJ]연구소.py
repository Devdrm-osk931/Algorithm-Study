# Samsung Study

"""
1. 벽 세우는 경우를 백트래킹으로 구한다
2. 각 바이러스 위치에서 전파를 시킨다
3. 안전 영역을 구한다
"""
from collections import deque

BLANK = 0
WALL = 1
VIRUS = 2
CNT = 3
answer = 0  # 안전영역의 최대값을 저장할 정답변수

# input
n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

copy = [
    row[:]
    for row in grid
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

candidates = [
    (i, j)
    for i in range(n)
    for j in range(m)
    if grid[i][j] == BLANK
]
limit = len(candidates)
selected = []


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(i, j):
    q = deque()

    q.append((i, j))
    visited[i][j] = True

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and grid[nx][ny] == BLANK and not visited[nx][ny]:
                grid[nx][ny] = VIRUS
                q.append((nx, ny))
                visited[nx][ny] = True


def case_computation():
    global answer

    # grid 초기화
    for i in range(n):
        for j in range(m):
            grid[i][j] = copy[i][j]
            visited[i][j] = False

    # 벽 세워주기
    for i, j in selected:
        grid[i][j] = WALL

    # BFS
    for i in range(n):
        for j in range(m):
            if grid[i][j] == VIRUS and not visited[i][j]:
                bfs(i, j)

    answer = max(answer, len([(i, j) for i in range(n) for j in range(m) if grid[i][j] == BLANK]))


def make_combination(idx, cnt):
    if cnt == CNT:
        case_computation()
        return
    if idx == limit:
        return

    # idx 선택하는경우
    selected.append(candidates[idx])
    make_combination(idx + 1, cnt + 1)
    selected.pop()

    # idx 선택하지 않는경우
    make_combination(idx + 1, cnt)


make_combination(0, 0)
print(answer)