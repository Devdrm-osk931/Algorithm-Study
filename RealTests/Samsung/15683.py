from collections import deque

BLANK = 0
WALL = 6
CHECK = 10

n, m = tuple(map(int, input().split()))
answer = n * m

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 상태를 되돌려주기 위한 원본 데이터
copied = [
    row[:]
    for row in grid
]

# 좌표 순서대로 배치된 cctv의 종류를 선정
cctvs = [
    grid[i][j]
    for i in range(n)
    for j in range(m)
    if grid[i][j] != BLANK and grid[i][j] != WALL
]

movements = [
    # 1번 cctv가 살필 수 있는 방향 4경우
    [[(-1, 0)], [(1, 0)], [(0, -1)], [(0, 1)]],
    # 2번 cctv가 살필 수 있는 방향 2경우
    [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]],
    # 3번 cctv가 살필 수 있는 방향 4경우
    [[(-1, 0), (0, 1)], [(-1, 0), (0, -1)], [(1, 0), (0, 1)], [(1, 0), (0, -1)]],
    # 4번 cctv가 살필 수 있는 방향 4경우
    [[(-1, 0), (0, -1), (0, 1)], [(1, 0), (0, -1), (0, 1)], [(0, 1), (-1, 0), (1, 0)], [(0, -1), (-1, 0), (1, 0)]],
    # 5번 cctv가 살필 수 있는 방향 1경우
    [[(-1, 0), (1, 0), (0, -1), (0, 1)]]
]

cctv_case_map = {
    1: 4,
    2: 2,
    3: 4,
    4: 4,
    5: 1
}

cctv_cnt = len(cctvs)
cases = []


def can_go(x, y):
    return 0 <= x < n and 0 <= y < m and grid[x][y] != WALL


def probe():
    mvs = deque(cases[:])
    for i in range(n):
        for j in range(m):
            # cctv라면
            if 1 <= grid[i][j] <= 5:
                curr_x, curr_y = i, j
                cctv_num = grid[i][j]
                mv = mvs.popleft()

                for dx, dy in movements[cctv_num - 1][mv]:
                    new_x = curr_x + dx
                    new_y = curr_y + dy

                    while can_go(new_x, new_y):
                        if grid[new_x][new_y] == CHECK or grid[new_x][new_y] == BLANK:
                            grid[new_x][new_y] = CHECK
                        new_x += dx
                        new_y += dy


def make_cases(idx):
    global grid, answer
    if idx == cctv_cnt:
        # init
        grid = [
            row[:]
            for row in copied
        ]
        # 각 씨씨티비 위치에서 정한 움직임 경우대로 움직이며 체크한다
        probe()
        # 탐색되지 않은 영역의 갯수를 구한다
        # print("=================")
        # for row in grid:
        #     for elem in row:
        #         print(elem, end=' ')
        #     print()
        not_searched = (len([
            (i, j)
            for i in range(n)
            for j in range(m)
            if grid[i][j] == 0
        ]))
        answer = min(answer, not_searched)
        return

    for i in range(cctv_case_map[cctvs[idx]]):
        cases.append(i)
        make_cases(idx + 1)
        cases.pop()


make_cases(0)
print(answer)