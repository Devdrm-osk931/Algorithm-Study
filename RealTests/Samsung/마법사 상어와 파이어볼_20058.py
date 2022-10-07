# BOJ 마법사 상어와 파이어볼 골드4
# Samsung
from collections import deque

n, q = tuple(map(int, input().split()))
n = 2 ** n
dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]
sum = 0

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

melt = [
    [False for _ in range(n)]
    for _ in range(n)
]

levels = list(map(int, input().split()))


# (i, j)를 좌상단 꼭지점으로 하고 길이가 unit인 배열을 오른쪽으로 90도 회전하는 함수
def rotate(i, j, unit):
    tmp = [row[j:j + unit] for row in grid[i:i+unit]]
    rev = tmp[::-1]
    rev = list(zip(*rev))

    for row in range(i, i + unit):
        for col in range(j, j + unit):
            grid[row][col] = rev[row - i][col - j]


def process(level):
    if level == 0:
        return

    unit = 2 ** level
    cnt = 1

    for i in range(0, n, unit):
        for j in range(0, n, unit):
            rotate(i, j, unit)


def in_range(i, j):
    return 0 <= i < n and 0 <= j < n


def more_than_three(i, j):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = i + dx, j + dy
        if in_range(nx, ny) and grid[nx][ny]:
            cnt += 1

    if cnt >= 3:
        return True
    else:
        return False


def print_grid():
    for row in grid:
        for elem in row:
            print(elem, end=' ')
        print()


def init_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0
            melt[i][j] = False


def simulate():
    for level in levels:
        init_visited()
        process(level)
        for i in range(n):
            for j in range(n):
                if not more_than_three(i, j) and grid[i][j]:
                    melt[i][j] = True

        for i in range(n):
            for j in range(n):
                if melt[i][j]:
                    grid[i][j] -= 1

def get_sum():
    global sum
    for row in grid:
        for elem in row:
            sum += elem
    print(sum)


def bfs(i, j):
    q = deque()
    cnt = 1
    visited[i][j] = cnt
    cnt += 1
    q.append((i, j))

    while q:
        curr_x, curr_y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = curr_x + dx, curr_y + dy

            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny]:
                visited[nx][ny] = cnt
                cnt += 1
                q.append((nx, ny))


def solve():
    simulate()
    get_sum()

    for i in range(n):
        for j in range(n):
            if grid[i][j] and not visited[i][j]:
                bfs(i, j)
    print(
        max([
            visited[i][j]
            for i in range(n)
            for j in range(n)
        ])
    )


solve()