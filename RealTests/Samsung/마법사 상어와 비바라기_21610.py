# BOJ 마법사 상어와 비바라기
# Samsung

n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

cmds = [list(map(int, input().split())) for _ in range(m)]

cloud = [
    [False for _ in range(n)]
    for _ in range(n)
]

cloud[n - 1][0], cloud[n - 1][1], cloud[n - 2][0], cloud[n - 2][1] = True, True, True, True

temp = [
    [False for _ in range(n)]
    for _ in range(n)
]

dxs = [0, -1, -1, -1, 0, 1, 1, 1]
dys = [-1, -1, 0, 1, 1, 1, 0, -1]

d_dxs = [-1, -1, 1, 1]
d_dys = [-1, 1, -1, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def init_temp():
    for row in range(n):
        for col in range(n):
            temp[row][col] = False


def simulate():
    for d, s in cmds:
        d -= 1

        # temp 배열 초기화
        init_temp()

        # 구름 이동
        for row in range(n):
            for col in range(n):
                if cloud[row][col]:
                    new_row, new_col = (row + n + dxs[d] * s) % n, (col + n + dys[d] * s) % n
                    temp[new_row][new_col] = True

        # 적용
        for row in range(n):
            for col in range(n):
                cloud[row][col] = temp[row][col]

        # 구름 위치에 물 증가
        prev_cloud = []
        for row in range(n):
            for col in range(n):
                if cloud[row][col]:
                    prev_cloud.append((row, col))
                    grid[row][col] += 1

        # 물이 증가한 칸에서 물 복사 버그 마법 수행
        increment_cnts = []
        for x, y in prev_cloud:
            cnt = 0
            # 대각선 탐색
            for dx, dy in zip(d_dxs, d_dys):
                nx, ny = x + dx, y + dy
                if not in_range(nx, ny):
                    continue
                if grid[nx][ny]:
                    cnt += 1
            increment_cnts.append(cnt)

        for (x, y), increment_cnt in zip(prev_cloud, increment_cnts):
            grid[x][y] += increment_cnt


        # 격자에 물이 2 이상인 위치에 구름을 만들면서 기존에 있던 위치는 없애준다
        for row in range(n):
            for col in range(n):
                if grid[row][col] >= 2 and not cloud[row][col]:
                    cloud[row][col] = True
                    grid[row][col] -= 2

                elif cloud[row][col]:
                    cloud[row][col] = False

    # 격자에 남아있는 물의 양을 구한다
    answer = 0
    for row in grid:
        for elem in row:
            answer += elem

    # 출력
    print(answer)


simulate()