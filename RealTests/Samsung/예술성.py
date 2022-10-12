# Codetree 예술성
# Samsung(2022 상반기 오전#2)
# https://www.codetree.ai/frequent-problems/artistry/description

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

temp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

group = [
    [0 for _ in range(n)]
    for _ in range(n)
]

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
]

groups = {}
score = 0

# 상하좌우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def init(arr):
    for x in range(n):
        for y in range(n):
            arr[x][y] = 0


def dfs(x, y, group_num, cnt):
    visited[x][y] = 1
    group[x][y] = group_num
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not visited[nx][ny] and grid[x][y] == grid[nx][ny]:
            cnt = dfs(nx, ny, group_num, cnt + 1)
    return cnt


def make_group():
    global groups
    groups = {}
    group_num = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group_num += 1
                group_cnt = dfs(i, j, group_num, 1)
                groups[group_num] = (group_cnt, grid[i][j])


def compute_artistry():
    global score
    for group_num in range(1, len(groups) + 1):
        adjacent = [0 for _ in range(len(groups) + 1)]
        for x in range(n):
            for y in range(n):
                if group[x][y] != group_num:
                    continue

                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if in_range(nx, ny):
                        if group[nx][ny] == group_num:
                            continue
                        if group[nx][ny] > group[x][y]:
                            adjacent[group[nx][ny]] += 1

        # group_num과 next_group_idx가 인접했다면 점수를 합산한다
        for next_group_idx in range(1, len(groups) + 1):
            if not adjacent[next_group_idx]:
                continue
            score += (groups[group_num][0] + groups[next_group_idx][0]) * groups[group_num][1] * groups[next_group_idx][1] * adjacent[next_group_idx]


def cross_ccw():
    for col in range(n - 1, -1, -1):
        temp[col][n//2] = grid[n//2][n - 1 - col]

    for row in range(n):
        temp[n//2][row] = grid[row][n//2]


def rotate_square(x, y, unit):
    for i in range(unit):
        for j in range(unit):
            temp[x + i][y + j] = grid[x + unit - 1 - j][y + i]


def rotate_squares():
    rotate_square(0, 0, n//2)
    rotate_square(0, n//2 + 1, n//2)
    rotate_square(n//2 + 1, 0, n//2)
    rotate_square(n//2 + 1, n//2 + 1, n//2)


# 예술성을 구하는 함수(1회)
def simulate():

    #1. 그룹을 지어서 group 배열에 기록한다
    init(group)
    init(visited)
    make_group()

    #2. 조화로움을 계산한다
    compute_artistry()

    #3. 십자 모양을 반시계 방향으로 회전한다
    init(temp)
    cross_ccw()

    #4. 십자 모양을 제외한 각 사각형을 90도 회전시킨다
    rotate_squares()

    # 5. temp 배열을 grid로 옮겨준다
    for row in range(n):
        for col in range(n):
            grid[row][col] = temp[row][col]


for _ in range(4):
    simulate()
print(score)