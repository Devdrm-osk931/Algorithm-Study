# BOJ 온풍기 안녕! Platinum5
# Samsung
from collections import deque

# Input
r, c, k = tuple(map(int, input().split()))

# 우/좌/상/하
dxs = [0, 0, -1, 1]
dys = [1, -1, 0, 0]
RIGHT, LEFT, UP, DOWN = 0, 1, 2, 3

grid = [
    list(map(int, input().split()))
    for _ in range(r)
]

# 온풍기 위치/방향 배열 & 조사 대상 칸
warmers = []
investigate = []

for x in range(r):
    for y in range(c):
        if grid[x][y] == 0:
            continue
        # 조사 대상 칸
        if grid[x][y] == 5:
            investigate.append((x, y))
        else:
            warmers.append((x, y, grid[x][y] - 1))
        grid[x][y] = 0


temp = [
    [0 for _ in range(c)]
    for _ in range(r)
]

# 벽 정보 설정 -> wall[x][y] -> (x,y) 위치에서의 벽 정보
wall = [
    # 오른쪽/왼쪽/위/아래
    [[0, 0, 0, 0] for _ in range(c)]
    for _ in range(r)
]

w = int(input())
for _ in range(w):
    # t:0 = (x - 1, y - 1) 위에 벽이 있다 , (x - 2, y - 1) 아래 벽이 있다
    # t:1 = (x - 1, y - 1) 오른쪽에 벽이 있다, (x - 1, y) 왼쪽에 벽이 있다
    x, y, t = tuple(map(int, input().split()))
    if t == 0:
        wall[x - 1][y - 1][UP] = 1
        wall[x - 2][y - 1][DOWN] = 1
    else:
        wall[x - 1][y - 1][RIGHT] = 1
        wall[x - 1][y][LEFT] = 1


# <함수 구현부>

def in_range(x, y):
    return 0 <= x < r and 0 <= y < c


def init_temp():
    for x in range(r):
        for y in range(c):
            temp[x][y] = 0


def reachable(x, y, d):
    points = []

    if d == UP:
        # x, y 를 기준으로 왼쪽에 벽이 없고 x, y - 1 위에 벽이 없으면 x - 1, y - 1 도달 가능 + 격자 내에 존재
        if in_range(x - 1, y - 1) and not wall[x][y][LEFT] and not wall[x][y - 1][UP]:
            points.append((x - 1, y - 1))

        if in_range(x - 1, y) and not wall[x][y][UP]:
            points.append((x - 1, y))

        if in_range(x - 1, y + 1) and not wall[x][y][RIGHT] and not wall[x][y + 1][UP]:
            points.append((x - 1, y + 1))

    elif d == DOWN:
        if in_range(x + 1, y - 1) and not wall[x][y][LEFT] and not wall[x][y - 1][DOWN]:
            points.append((x + 1, y - 1))

        if in_range(x + 1, y) and not wall[x][y][DOWN]:
            points.append((x + 1, y))

        if in_range(x + 1, y + 1) and not wall[x][y][RIGHT] and not wall[x][y + 1][DOWN]:
            points.append((x + 1, y + 1))

    elif d == RIGHT:
        if in_range(x - 1, y + 1) and not wall[x][y][UP] and not wall[x - 1][y][RIGHT]:
            points.append((x - 1, y + 1))

        if in_range(x, y + 1) and not wall[x][y][RIGHT]:
            points.append((x , y + 1))

        if in_range(x + 1, y + 1) and not wall[x][y][DOWN] and not wall[x + 1][y][RIGHT]:
            points.append((x + 1, y + 1))

    else:
        if in_range(x - 1, y - 1) and not wall[x][y][UP] and not wall[x - 1][y][LEFT]:
            points.append((x - 1, y - 1))

        if in_range(x, y - 1) and not wall[x][y][LEFT]:
            points.append((x, y - 1))

        if in_range(x + 1, y - 1) and not wall[x][y][DOWN] and not wall[x + 1][y][LEFT]:
            points.append((x + 1, y - 1))

    return points


def activate(x, y, d):
    queue = deque()
    # temp 배열 초기화
    init_temp()
    # 맨 처음에 x, y 에서 d 방향으로 5
    x, y = x + dxs[d], y + dys[d]
    temp[x][y] = 5
    queue.append((x, y))

    while queue:
        px, py = queue.popleft()

        # 각 점에서 세가지 경우를 확인한다
        possible_points = reachable(px, py, d)
        for nx, ny in possible_points:
            temp[nx][ny] = temp[px][py] - 1
            if temp[nx][ny] > 1:
                queue.append((nx, ny))

    # temp -> grid
    for x in range(r):
        for y in range(c):
            grid[x][y] += temp[x][y]


def adjust_temperature():
    # 기존의 grid상태를 temp에 복사한다
    for x in range(r):
        for y in range(c):
            temp[x][y] = grid[x][y]

    # grid를 기준으로 각 점에서 4방향을 비교하며 자신보다 작은 격자를 찾으면 차이/4만큼 + - 한 것을 temp에 반영한다
    for x in range(r):
        for y in range(c):
            cx, cy = x, y

            # 0, 1, 2, 3 순서 -> 우 좌 상 하 -> i 방향 보려면 cx, cy 의 i 방향에 벽이 없어야함
            for i in range(4):
                nx, ny = cx + dxs[i], cy + dys[i]
                if in_range(nx, ny) and not wall[cx][cy][i] and grid[x][y] > grid[nx][ny]:
                    change = (grid[x][y] - grid[nx][ny]) // 4
                    temp[x][y] -= change
                    temp[nx][ny] += change

    # temp를 다시 grid로 옮긴다
    for x in range(r):
        for y in range(c):
            grid[x][y] = temp[x][y]


def lower_outer():
    # 최상단과 최하단을 확인한다
    for y in range(c):
        if grid[0][y] > 0:
            grid[0][y] -= 1
        if grid[r - 1][y] > 0:
            grid[r - 1][y] -= 1

    # 최좌측과 최우측을 확인한다
    for x in range(1, r - 1):
        if grid[x][0] > 0:
            grid[x][0] -= 1
        if grid[x][c - 1] > 0:
            grid[x][c - 1] -= 1


def check():
    for x, y in investigate:
        if grid[x][y] < k:
            return False

    return True


def simulate():
    chocolate = 0
    while True:
        # 1. 각 온풍기 작동, 온기 합산
        for x, y, d in warmers:
            activate(x, y, d)

        # 2. 온도를 조절한다
        adjust_temperature()

        # 3. 가장 바깥 온도를 1씩 감소시킨다
        lower_outer()

        # 4. 초콜릿을 하나 먹는다
        chocolate += 1

        # 5. 관찰 대상 격자의 온도가 모두 K보다 크거나 같은지 확인한다
        if check():
            break

        # 먹은 초콜릿 갯수가 100보다 크다면 더이상 볼 필요 없이 101 출력할것이므로 탈출
        if chocolate > 100:
            break

    if chocolate > 100:
        print(101)
    else:
        print(chocolate)


simulate()
