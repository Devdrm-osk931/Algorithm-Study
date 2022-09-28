# BOJ20056 마법사 상어와 파이어볼 Gold4
# Samsung

N, M, K = tuple(map(int, input().split()))

dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
dys = [0, 1, 1, 1, 0, -1, -1, -1]

grid = [
    [[] for _ in range(N)]
    for _ in range(N)
]

next_grid = [
    [[] for _ in range(N)]
    for _ in range(N)
]

for _ in range(M):
    r, c, m, s, d = tuple(map(int, input().split()))
    grid[r - 1][c - 1].append([m, s, d])


def print_grid():
    for row in grid:
        for elem in row:
            print(elem, end=' ')
        print()


def init_next_grid():
    for row in range(N):
        for col in range(N):
            next_grid[row][col] = []


def move():
    # next_grid 초기화
    init_next_grid()

    # grid를 순회하며 각 파이어볼에 대해 다음 위치를 계산하여 Next_grid에 옮긴다
    for row in range(N):
        for col in range(N):
            if not grid[row][col]:
                continue

            for fireball in grid[row][col]:
                curr_x, curr_y = row, col
                m, s, d = fireball

                # 다음 위치 계산
                next_x = (curr_x + N + dxs[d] * s) % N
                next_y = (curr_y + N + dys[d] * s) % N

                next_grid[next_x][next_y].append([m, s, d])

    # 2개 이상의 파이어볼이 있는 칸에서의 작업
    for row in range(N):
        for col in range(N):
            if len(next_grid[row][col]) <= 1:
                continue

            all_same = True
            prev_dir = -1
            total_m = 0
            total_s = 0
            fireball_cnt = 0

            while next_grid[row][col]:
                fireball_cnt += 1
                m, s, d = next_grid[row][col].pop()
                total_m += m
                total_s += s
                if prev_dir == -1:
                    prev_dir = d % 2
                else:
                    if prev_dir != d % 2:
                        all_same = False

            new_m = total_m // 5
            new_s = total_s // fireball_cnt

            # 무게가 0이 되면 추가 작업을 하지 않고 넘어간다
            if new_m == 0:
                continue

            if all_same:
                for new_d in [0, 2, 4, 6]:
                    next_grid[row][col].append([new_m, new_s, new_d])
            else:
                for new_d in [1, 3, 5, 7]:
                    next_grid[row][col].append([new_m, new_s, new_d])

    # next_grid를 grid로 옮겨준다
    for row in range(N):
        for col in range(N):
            grid[row][col] = next_grid[row][col][:]


def get_weight():
    weight = 0
    for row in range(N):
        for col in range(N):
            if not grid[row][col]:
                continue
            for m, _, _ in grid[row][col]:
                weight += m
    return weight


def simulate():
    for _ in range(K):
        move()

    answer = get_weight()
    print(answer)
    return


simulate()
