# BOJ 연구소3 골드4
# Samsung
import sys
from collections import deque

BLANK = 0
WALL = 1
VIRUS = 2

n, m = tuple(map(int, input().split()))
answer = sys.maxsize

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

copy = [
        row[:]
        for row in grid
    ]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

dist = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 바이러스가 위치할 수 있는 모든 후보 좌표
virus_positions = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == VIRUS
]

virus_cnt = len(virus_positions)


def init():
    for i in range(n):
        for j in range(n):
            grid[i][j] = copy[i][j]
            visited[i][j] = False
            dist[i][j] = 0


case = []
dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def can_go(x, y):
    return in_range(x, y) and grid[x][y] != WALL and not visited[x][y]


def blank_exist():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == BLANK and visited[i][j] == False:
                return True
    return False


def case_simulation():
    global answer

    queue = deque()
    init()
    for i, j in case:
        queue.append((i, j))
        visited[i][j] = True
        dist[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

    # BFS를 수행한 뒤 빈칸이 존재하는지 확인한다
    if blank_exist():
        return
    # 빈칸 중 최대값을 answer와 비교하여 최소값을 취한다

    case_maximum = max([
        dist[i][j]
        for i in range(n)
        for j in range(n)
        if grid[i][j] == BLANK or (i, j) in case
    ])

    answer = min(answer, case_maximum)




def solve(idx, cnt):
    if cnt == m:
        case_simulation()
        return
    if idx == virus_cnt:
        return

    # idx 번째 바이러스를 선택하지 않을 경우
    solve(idx + 1, cnt)

    # idx번째 바이러스를 선택할 경우
    case.append(virus_positions[idx])
    solve(idx + 1, cnt + 1)
    case.pop()


solve(0, 0)
if answer == sys.maxsize:
    print(-1)
else:
    print(answer)