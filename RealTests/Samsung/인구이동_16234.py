from collections import deque

# 변수 입력
n, left, right = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
queue = deque()
dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]
moved = False
answer = 0


# 방문 체크 배열을 초기화한다
def reset():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def can_go(x, y):
    return in_range(x, y) and not visited[x][y]


def print_grid():
    for row in grid:
        for elem in row:
            print(elem, end=' ')
        print()
    print()


# (i, j)를 시작으로 bfs를 수행한다
def group(i, j):
    global moved
    sum, cnt = 0, 0
    grouped = []
    queue.append((i, j))
    visited[i][j] = True

    while queue:
        x, y = queue.popleft()
        sum += grid[x][y]
        cnt += 1
        grouped.append((x, y))
        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy
            if can_go(nx, ny) and left <= abs(grid[nx][ny] - grid[x][y]) <= right:
                moved = True
                visited[nx][ny] = True
                queue.append((nx, ny))
    k = sum // cnt
    for x, y in grouped:
        grid[x][y] = k


def move():
    reset()
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group(i, j)


def simulate():
    global answer, moved
    while True:
        move()
        if moved:
            answer += 1
            moved = False
        else:
            break

    print(answer)

simulate()

