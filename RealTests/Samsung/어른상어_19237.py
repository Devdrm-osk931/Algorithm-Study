# BOJ 19237 어른상어 골드2
# Samsung
def process(num):
    if int(num) != 0:
        return int(num) - 1
    return int(num)

BLANK = 0
answer = 0

# N x N 격자에 M 마리의 상어가 있고 상어 냄새는 k초 동안 지속된다
N, M, k = tuple(map(int, input().split()))

# 격자의 모습이 주어진다
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

next_grid = [
    [[] for _ in range(N)]
    for _ in range(N)
]

smell = [
    [0 for _ in range(N)]
    for _ in range(N)
]

# 처음 위치에 냄새 설정
for i in range(N):
    for j in range(N):
        if grid[i][j] != 0:
            shark_num = grid[i][j]
            smell[i][j] = [shark_num, k]


# 0, 1, 2, 3 => 위 아래 왼쪽 오른쪽
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
curr_dirs = list(map(process, input().split()))

# priorities[shark_num][curr_dir] -> 상어의 현 방향에서의 우선순위
priorities = [
    [
        list(map(process, input().split()))
        for _ in range(4)
    ]
    for _ in range(M)
]


def done():
    for i in range(N):
        for j in range(N):
            if grid[i][j] != BLANK and grid[i][j] != 1:
                return False
    return True


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def init_next_grid():
    for i in range(N):
        for j in range(N):
            next_grid[i][j] = []


# 상어를 하나씩 움직인다
def move_shark(shark_num, i, j):
    x, y = i, j
    shark_dir = curr_dirs[shark_num - 1]

    # 현재 방향을 기준으로 4방향을 살펴서 갈 수 있는 곳을 찾는다
    for dir_num in priorities[shark_num - 1][shark_dir]:
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

        # 진행할 수 있는 빈칸을 탐색한다
        if in_range(nx, ny) and smell[nx][ny] == BLANK:
            # nx, ny 위치로 상어를 이동시킨다
            next_grid[nx][ny].append(shark_num)
            curr_dirs[shark_num - 1] = dir_num
            return

    # 그런 칸이 없다면 차선책으로 본인 냄새가 있는 위치를 찾는다
    for dir_num in priorities[shark_num - 1][shark_dir]:
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

        if in_range(nx, ny) and smell[nx][ny][0] == shark_num:
            # nx, ny 위치로 상어를 이동시킨다
            next_grid[nx][ny].append(shark_num)
            curr_dirs[shark_num - 1] = dir_num
            return


def move_sharks():
    # 임시 배열 초기화
    init_next_grid()

    # 상어가 있는 위치를 찾게되면 상어를 움직여준다
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 0:
                shark_num = grid[i][j]
                move_shark(shark_num, i, j)

    # 냄새를 하나씩 감소시킨다
    for i in range(N):
        for j in range(N):
            if smell[i][j]:
                # 감소해서 0이 되면 빈칸으로 만들어줌
                if smell[i][j][1] == 1:
                    smell[i][j] = 0
                else:
                    smell[i][j][1] -= 1

    # 임시 격자에서 현재 격자로 옮겨주며 냄새를 새겨준다
    for i in range(N):
        for j in range(N):
            if next_grid[i][j]:
                next_grid[i][j].sort()
                grid[i][j] = next_grid[i][j][0]
                smell[i][j] = [grid[i][j], k]
            else:
                grid[i][j] = 0


def simulate():
    global answer
    while answer < 1000:
        answer += 1
        move_sharks()
        if done():
            print(answer)
            return

    print(-1)


simulate()