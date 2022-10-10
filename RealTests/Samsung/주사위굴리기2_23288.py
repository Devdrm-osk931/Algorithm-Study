# BOJ 주사위 굴리기 2
# Samsung

# 격자/움직임 정보 입력
n, m, k = tuple(map(int, input().split()))
move_cnt = 0
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

# 4방향 입력 -> 상/좌/우/하
dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

# 초기 설정: (0, 0), 동쪽
cx, cy = 0, 0
curr_dir = 2
top, front, right, bottom, back, left = 1, 5, 3, 6, 2, 4
score = 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def move():
    global cx, cy, curr_dir
    # 현재 방향으로 이동이 가능한지 확인한다
    nx, ny = cx + dxs[curr_dir], cy + dys[curr_dir]
    if not in_range(nx, ny):
        curr_dir = 3 - curr_dir
        nx, ny = cx + dxs[curr_dir], cy + dys[curr_dir]

    # 위치 갱신
    cx, cy = nx, ny


# direction 방향으로 이동되었을 때 변하는 주사위의 모습
def renew_dice(direction):
    global top, front, right, bottom, back, left
    # 위로 돌리는 경우
    if direction == 0:
        top, front, right, bottom, back, left = front, bottom, right, back, top, left
    # 아래로 돌리는 경우
    elif direction == 3:
        top, front, right, bottom, back, left = back, top, right, front, bottom, left
    # 왼쪽으로 돌리는 경우
    elif direction == 1:
        top, front, right, bottom, back, left = right, front, bottom, left, back, top
    # 오른쪽으로 돌리는 경우
    else:
        top, front, right, bottom, back, left = left, front, top, right, back, bottom


def reachable(x, y, cnt, start_x, start_y):
    visited[x][y] = True
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] == grid[start_x][start_y]:
            cnt = reachable(nx, ny, cnt + 1, start_x, start_y)
    return cnt


def init_visited():
    for row in range(n):
        for col in range(m):
            visited[row][col] = False


def add_score():
    global score
    init_visited()
    A, B = reachable(cx, cy, 1, cx, cy), grid[cx][cy]
    score += A * B


# 방향 순서: 상 좌 우 하
def update_direction():
    global curr_dir

    on_grid = grid[cx][cy]
    on_bottom = bottom

    # 이동방향 90도 시계방향으로 회전
    if on_bottom > on_grid:
        if curr_dir == 0:
            curr_dir = 2
        elif curr_dir == 1:
            curr_dir = 0
        elif curr_dir == 2:
            curr_dir = 3
        else:
            curr_dir = 1

    # 이동방향 90도 반시계방향으로 회전
    elif on_bottom < on_grid:
        if curr_dir == 0:
            curr_dir = 1
        elif curr_dir == 1:
            curr_dir = 3
        elif curr_dir == 2:
            curr_dir = 0
        else:
            curr_dir = 2


def simulate():
    global move_cnt
    while move_cnt < k:
        # 1 현재 방향을 기준으로 갈 수 있다면 가고, 없다면 반대 방향으로 바꿔서 한 칸 이동한다
        move()

        # 2 이동한 방향에 대해 주사위의 형태를 업데이트 해준다
        renew_dice(curr_dir)

        # 2 점수를 획득한다
        add_score()

        # 3 다음 이동 방향을 선정한다
        update_direction()
        move_cnt += 1

    print(score)


simulate()