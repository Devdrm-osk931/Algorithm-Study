WHITE = 0
RED = 1
BLUE = 2

# 1, 2, 3, 4 -> 오른쪽 왼쪽 위 아래
dxs = [0, 0, 0, -1, 1]
dys = [0, 1, -1, 0, 0]

turns = 0

n, k = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

pos = [
    [[] for _ in range(n)]
    for _ in range(n)
]

for pawn_num in range(k):
    r, c, dir = tuple(map(int, input().split()))
    pos[r - 1][c - 1].append([pawn_num + 1, dir])


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def get_opposite(curr_dir):
    if curr_dir == 1:
        return 2
    elif curr_dir == 2:
        return 1
    elif curr_dir == 3:
        return 4
    else:
        return 3


def clear():
    for i in range(n):
        for j in range(n):
            if len(pos[i][j]) >= 4:
                return True
    return False


def find_location(pawn_num):
    for i in range(n):
        for j in range(n):
            if not pos[i][j]:
                continue

            for idx in range(len(pos[i][j])):
                if pos[i][j][idx][0] == pawn_num:
                    return i, j, idx


def move(pawn_num):
    curr_x, curr_y, idx = find_location(pawn_num)
    curr_dir = pos[curr_x][curr_y][idx][1]

    # 다음 위치를 확인한다
    next_x, next_y = curr_x + dxs[curr_dir], curr_y + dys[curr_dir]

    # 다음 위치가 격자 밖이거나 파란색인 경우 한번은 반대 방향으로 돌린뒤 살펴본다
    if not in_range(next_x, next_y) or grid[next_x][next_y] == BLUE:
        # 반대 방향을 살펴본다
        pos[curr_x][curr_y][idx][1] = get_opposite(curr_dir)
        curr_dir = pos[curr_x][curr_y][idx][1]
        next_x, next_y = curr_x + dxs[curr_dir], curr_y + dys[curr_dir]

    # 세가지 경우를 살핀다
    # 1. 다음 위치가 격자 밖이거나 파란색인 경우 - 움직이지 않는다
    if not in_range(next_x, next_y) or grid[next_x][next_y] == BLUE:
        return

    target = pos[curr_x][curr_y][idx:]
    pos[curr_x][curr_y] = pos[curr_x][curr_y][:idx]
    # 2. 다음 위치가 흰색인 경우
    if grid[next_x][next_y] == WHITE:
        pos[next_x][next_y] += target
        return
    if grid[next_x][next_y] == RED:
        pos[next_x][next_y] += target[::-1]
        return


def simulate():
    global turns

    if clear():
        print(turns)
        return

    while turns < 1000:
        turns += 1

        for pawn_num in range(1, k + 1):
            move(pawn_num)
            if clear():
                print(turns)
                return

    print(-1)
    return


simulate()