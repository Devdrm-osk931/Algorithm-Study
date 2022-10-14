# import

# 전역변수
N = 4

# 물고기 움직임
# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dxs = [0, -1, -1, -1, 0, 1, 1, 1]
dys = [-1, -1, 0, 1, 1, 1, 0, -1]

# 상어 움직임 - 상 좌 하 우
sdxs = [-1, 0, 1, 0]
sdys = [0, -1, 0, 1]

# 함수부
def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def move_to_temp():
    for i in range(N):
        for j in range(N):
            temp[i][j] = []
            temp_fish[i][j] = []
            if not grid[i][j]:
                continue
            for elem in grid[i][j]:
                temp[i][j].append(elem)


def move_fish(i, j, dir):
    curr_x, curr_y, curr_dir = i, j, dir

    for c in range(8):
        new_dir = (curr_dir + 8 - c) % 8
        nx, ny = curr_x + dxs[new_dir], curr_y + dys[new_dir]
        # 격자 내에 존재 & 상어 위치가 아님 & 물고기의 냄새가 있으면 안됨
        if in_range(nx, ny) and (nx, ny) != (sx, sy) and not smell[nx][ny]:
            curr_x, curr_y, curr_dir = nx, ny, new_dir
            break

    temp_fish[curr_x][curr_y].append(curr_dir)


def move_all_fish():
    # temp 격자를 순회하며 물고기가 있는 위치를 찾는다
    for i in range(N):
        for j in range(N):
            # 물고기가 없다면 무시한다
            if not temp[i][j]:
                continue

            # 존재하는 물고기를 temp_fish에 기록한다
            for curr_dir in temp[i][j]:
                # i, j에서 방향이 fish_dirction인 물고기를 움직인다
                move_fish(i, j, curr_dir)

    # temp_fish에 기록한 움직임을 temp에 덮어씌워준다
    update_temp()


# 물고기의 움직임을 temp에 반영한다: temp_fish -> temp
def update_temp():
    for i in range(N):
        for j in range(N):
            temp[i][j] = []
            if not temp_fish[i][j]:
                continue
            for d in temp_fish[i][j]:
                temp[i][j].append(d)


# 움직임 우선순위-> 상 좌 하 우
def move_shark(x, y, depth, catch_cnt, visited):
    global sx, sy, max_eat, eat
    if depth == 3:
        if catch_cnt > max_eat:
            max_eat = catch_cnt
            eat = visited[:]
            sx, sy = x, y
        return

    for sdx, sdy in zip(sdxs, sdys):
        nx, ny = x + sdx, y + sdy
        if in_range(nx, ny):
            if (nx, ny) in visited:
                move_shark(nx, ny, depth + 1, catch_cnt, visited)
            else:
                visited.append((nx, ny))
                move_shark(nx, ny, depth + 1, catch_cnt + len(temp[nx][ny]), visited)
                visited.pop()


def eat_put_smell():
    global i, j
    for i, j in eat:
        if temp[i][j]:
            temp[i][j] = []
            smell[i][j] = 3


def remove_smell():
    global i, j
    for i in range(N):
        for j in range(N):
            if smell[i][j] > 0:
                smell[i][j] -= 1


def duplicate():
    global i, j
    for i in range(N):
        for j in range(N):
            if not temp[i][j]:
                continue
            for elem in temp[i][j]:
                grid[i][j].append(elem)

# tc = int(input())
# for t in range(tc):
# 코드부
M, S = tuple(map(int, input().split()))

grid = [
    [[] for _ in range(N)]
    for _ in range(N)
]

temp = [
    [[] for _ in range(N)]
    for _ in range(N)
]

temp_fish = [
    [[] for _ in range(N)]
    for _ in range(N)
]

smell = [
    [0 for _ in range(N)]
    for _ in range(N)
]

# 물고기 위치 grid에 저장
for _ in range(M):
    fx, fy, d = tuple(map(int, input().split()))
    grid[fx - 1][fy - 1].append(d - 1)

# 상어 위치 입력
sx, sy = tuple(map(int, input().split()))
sx, sy = sx - 1, sy - 1


# S 번 마법을 시전한다
for _ in range(S):
    max_eat = -1
    eat = []
    # 1. 복제 마법 시전 - grid를 유지하고 작업을 temp에서 진행한다(초기화 작업도 포함됨)
    move_to_temp()

    # 2. 격자에 존재하는 물고기를 움직인다
    move_all_fish()

    # 3. 상어를 움직인다
    # 현재 상어의 위치(sx, sy)를 기준으로 3칸을 움직이면서 최적의 루트를 찾는다
    move_shark(sx, sy, 0, 0, [])

    # 4. 3에서 찾은 경로에 있는 물고기들을 없애고, 냄새를 남긴다
    eat_put_smell()

    # 5. 모든 냄새 하나씩 감소
    remove_smell()

    # 6. temp를 원 격자에 반영해준다
    duplicate()

# 남아있는 물고기의 수를 구한다
print(sum([
    len(grid[i][j])
    for i in range(N)
    for j in range(N)
    if grid[i][j]
]))
