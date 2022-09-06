# Samsung
# BOJ 17144
FRESH = 0
MACHINE = -1

r, c, t = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(r)
]

next_grid = [
    [0 for _ in range(c)]
    for _ in range(r)
]

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


def init_next_grid():
    for i in range(r):
        for j in range(c):
            next_grid[i][j] = grid[i][j]


def transfer():
    for i in range(r):
        for j in range(c):
            grid[i][j] = next_grid[i][j]


def diffuse():
    # next_grid 초기화
    init_next_grid()

    for i in range(r):
        for j in range(c):
            # (i, j) 위치가 먼지라면 확산을 해야한다
            if grid[i][j] != FRESH and grid[i][j] != MACHINE:
                amount = grid[i][j] // 5
                for dx, dy in zip(dxs, dys):
                    nx, ny = i + dx, j + dy
                    # 격자 내에 존재하고 해당 위치가 공기청정기가 아니라면 확산이 일어날 수 있다
                    if in_range(nx, ny) and grid[nx][ny] != MACHINE:
                        next_grid[nx][ny] += amount
                        next_grid[i][j] -= amount

    # 원래 격자로 옮긴다
    transfer()


def find_machine():
    # 공기 청정기의 위치를 찾는다
    locations = []
    for row in range(r):
        if grid[row][0] == MACHINE:
            locations.append((row, 0))

    return locations[0], locations[1]


def refresh():
    (ur, uc), (dr, dc) = find_machine()

    # Upper Half
    #left
    for row in range(ur, 0, -1):
        grid[row][0] = grid[row - 1][0]
    grid[ur][uc] = - 1
    #top
    for col in range(c - 1):
        grid[0][col] = grid[0][col + 1]
    #right
    for row in range(ur):
        grid[row][c-1] = grid[row + 1][c - 1]
    #bottom
    for col in range(c - 1, 1, -1):
        grid[ur][col] = grid[ur][col - 1]
    grid[ur][1] = 0

    # Lower Half
    #left
    for row in range(dr, r-1):
        grid[row][0] = grid[row + 1][0]
    grid[dr][dc] = -1
    #down
    for col in range(c - 1):
        grid[r - 1][col] = grid[r - 1][col + 1]
    #right
    for row in range(r - 1, dr, -1):
        grid[row][c - 1] = grid[row - 1][c - 1]
    #top
    for col in range(c - 1, 1, -1):
        grid[dr][col] = grid[dr][col - 1]
    grid[dr][1] = 0


def simulate():
    # 모든 미세먼지들에 대해 확산이 일어난다
    diffuse()
    refresh()


for _ in range(t):
    simulate()

answer = sum([
    grid[i][j]
    for i in range(r)
    for j in range(c)
    if grid[i][j] != -1
])

print(answer)