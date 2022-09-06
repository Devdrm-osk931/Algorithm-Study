# BOJ 17143
# Samsung 낚시왕 골드1

r, c, m = tuple(map(int, input().split()))
answer = 0

# 위, 아래, 오른쪽, 왼쪽
dxs = [0, -1, 1, 0, 0]
dys = [0, 0, 0, 1, -1]

grid = [
    [[] for _ in range(c)]
    for _ in range(r)
]

next_grid = [
    [[] for _ in range(c)]
    for _ in range(r)
]

for _ in range(m):
    row, col, speed, direction, size = tuple(map(int, input().split()))
    grid[row - 1][col - 1].append((speed, direction, size))


# 특정 col 에 위치한 상어 중 맨 위에 있는 상어를 잡는 함수
def catch_top(col):
    global answer
    for row in range(r):
        if len(grid[row][col]) > 0:
            _, _, size = grid[row][col].pop()
            answer += size
            return
    return


def init_next_grid():
    for i in range(r):
        for j in range(c):
            next_grid[i][j] = []


def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


def change(direction):
    if direction == 1:
        return 2
    elif direction == 2:
        return 1
    elif direction == 3:
        return 4
    else:
        return 3


def move(i, j):
    curr_x, curr_y = i, j
    speed, direction, size = grid[i][j][0]
    for _ in range(speed):
        next_x, next_y = curr_x + dxs[direction], curr_y + dys[direction]
        if in_range(next_x, next_y):
            curr_x, curr_y = next_x, next_y
        else:
            direction = change(direction)
            curr_x, curr_y = curr_x + dxs[direction], curr_y + dys[direction]

    next_grid[curr_x][curr_y].append((speed, direction, size))


def move_all():
    # next_grid 초기화
    init_next_grid()

    # 상어가 존재한다면 상어를 해당 속도로 이동한다
    for i in range(r):
        for j in range(c):
            if grid[i][j]:
                move(i, j)

    # next_grid -> grid, 한 칸에 여러 상어가 존재한다면 제일 큰 상어만 남긴다
    for i in range(r):
        for j in range(c):
            if len(next_grid[i][j]) > 1:
                next_grid[i][j].sort(key=lambda x:x[2], reverse=True)  # size 순서대로 내림차순 정렬
            grid[i][j] = next_grid[i][j][:1]

def simulate():
    # 0 ~ c - 1 까지의 열에 대해 수행
    for col in range(c):
        catch_top(col)
        move_all()
    print(answer)


# ---- MAIN ----
simulate()
