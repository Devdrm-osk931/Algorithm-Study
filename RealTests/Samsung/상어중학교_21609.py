# BOJ 상어중학교
# Samsung

N, M = tuple(map(int, input().split()))

COLOR = {i for i in range(1, M + 1)}
RAINBOW = 0
BLACK = -1
BLANK = -2

grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

visited = [
    [False for _ in range(N)]
    for _ in range(N)
]

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

# 그룹 선정 기준
group = []  # 가장 큰 그룹 덩어리에 속한 점들을 저장해줄 배열
s_row, s_col = N, N  # 그룹의 기준 행, 열
s_rainbow_cnt = 0  # 그룹 내 무지개블록 수


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def init_visited():
    global group
    for x in range(N):
        for y in range(N):
            visited[x][y] = False


def init_group():
    global group
    group = []


def dfs(x, y, result, target_color):
    visited[x][y] = True
    result.append((x, y))

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if in_range(nx, ny) and not visited[nx][ny] and (grid[nx][ny] == target_color or grid[nx][ny] == RAINBOW):
            dfs(nx, ny, result, target_color)

    return result


def get_standard(case_group):
    case_s_row, case_s_col = N, N
    case_rainbow_cnt = 0
    for x, y in case_group:
        if grid[x][y] == RAINBOW:
            case_rainbow_cnt += 1
            continue
        if (x, y) < (case_s_row, case_s_col):
            case_s_row, case_s_col = x, y

    return case_s_row, case_s_col, case_rainbow_cnt


def make_group():
    global group, s_row, s_col, s_rainbow_cnt
    grouped = False

    for i in range(N):
        for j in range(N):
            init_visited()
            if grid[i][j] in COLOR and not visited[i][j]:
                case_group = dfs(i, j, [], grid[i][j])

                if len(case_group) <= 1:
                    continue

                grouped = True

                # case_group에 대한 기준값들을 구한다
                case_s_row, case_s_col, case_rainbow_cnt = get_standard(case_group)

                # group의 크기가 더 큰 것으로 설정
                if len(case_group) > len(group):
                    group = case_group[:]
                    s_row, s_col, s_rainbow_cnt = case_s_row, case_s_col, case_rainbow_cnt

                # group 크기가 같다면 무지개 블록이 더 많은 쪽을 선정
                elif len(case_group) == len(group) and case_rainbow_cnt != s_rainbow_cnt:

                    if case_rainbow_cnt > s_rainbow_cnt:
                        group = case_group[:]
                        s_row, s_col, s_rainbow_cnt = case_s_row, case_s_col, case_rainbow_cnt

                # group 크기와 무지개 블록 수가 모두 같다면 기준행/열을 비교한다
                elif len(case_group) == len(group) and case_rainbow_cnt == s_rainbow_cnt:
                    if (case_s_row, case_s_col) > (s_row, s_col):
                        group = case_group[:]
                        s_row, s_col, s_rainbow_cnt = case_s_row, case_s_col, case_rainbow_cnt

    return grouped


def delete_group():
    for x, y in group:
        grid[x][y] = BLANK


def drop():
    temp = [
        [BLANK for _ in range(N)]
        for _ in range(N)
    ]

    for row in range(N):
        for col in range(N):
            if grid[row][col] == BLACK:
                temp[row][col] = BLACK

    for col in range(N):
        next_row = N - 1
        for row in range(N - 1, -1, -1):
            if grid[row][col] == BLACK:
                next_row = row - 1
                continue
            elif grid[row][col] in COLOR or grid[row][col] == RAINBOW:
                temp[next_row][col] = grid[row][col]
                next_row -= 1

    for row in range(N):
        for col in range(N):
            grid[row][col] = temp[row][col]


def rotate_CCW():
    temp = [
        [BLANK for _ in range(N)]
        for _ in range(N)
    ]

    # 변환 공식
    for row in range(N):
        for col in range(N):
            temp[N - 1 - col][row] = grid[row][col]

    # 옮기기
    for row in range(N):
        for col in range(N):
            grid[row][col] = temp[row][col]


def simulate():
    global group
    total_score = 0
    while True:
        group = []
        is_grouped = make_group()
        if not is_grouped:
            print(total_score)
            return
        # 가장 큰 그룹 안에 있는 점들을 모두 없애준다
        delete_group()
        total_score += len(group) ** 2

        # 중력에 의해 떨어트려준다
        drop()

        # 반시계 방향으로 한번 회전한다
        rotate_CCW()

        # 중력에 의해 떨어트려준다
        drop()


simulate()
