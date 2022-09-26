BLANK = 0
WALL = 1

# 입력
N, M = tuple(map(int, input().split()))

x, y, curr_dir = tuple(map(int, input().split()))

# 장소 정보
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

# 청소 여부 확인
cleaned = [
    [False for _ in range(M)]
    for _ in range(N)
]

# 북 동 남 서
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

# 이동 여부
moved = False


# 격자 내에 존재, 벽 아님, 아직 청소 x
def in_range(x, y):
    return 0 <= x < N and 0 <= y < M


def can_clean(x, y):
    return in_range(x, y) and grid[x][y] != WALL and not cleaned[x][y]


def get_next_pos():
    global moved, x, y, curr_dir
    moved = False

    # 현재 위치를 기준으로 왼쪽으로 탐색
    for i in range(1, 5):
        next_dir = (curr_dir + 4 - i) % 4
        nx, ny = x + dxs[next_dir], y + dys[next_dir]

        if can_clean(nx, ny):
            moved = True
            x, y, curr_dir = nx, ny, next_dir
            return moved

    # 4방향 모두 청소가 불가능하다면 후진이 가능한지 확인한다
    if not moved:
        back_dir = (curr_dir + 2) % 4
        nx, ny = x + dxs[back_dir], y + dys[back_dir]

        # 뒤쪽이 벽이 아니라면 그 곳으로 방향을 유지한 채로 돌아간다
        if grid[nx][ny] != WALL:
            moved = True
            x, y = nx, ny
            return moved

        else:
            moved = False
            return moved


def simulate():
    while True:
        # 1. 현재 위치를 청소한다
        if not cleaned[x][y]:
            cleaned[x][y] = True

        # 2. 다음 위치와 방향을 구한다, 만약 더이상 진행이 안된다면 while loop 탈출
        if not get_next_pos():
            break

    # 청소한 영역을 구한다
    print(len([(i, j) for i in range(N) for j in range(M) if cleaned[i][j]]))


simulate()