# 전역변수
# 상하좌우
import sys

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
cctvs = [
    [],
    [[0], [1], [2], [3]], # 1번 cctv 가능한 방향
    [[0, 1], [2, 3]], # 2번 cctv 가능한 방향
    [[0, 3], [2, 0], [2, 1], [1, 3]],  # 3번 cctv 가능한 방향
    [[0, 2, 3], [2, 0, 1], [1, 2, 3], [3, 0, 1]],  # 4번 cctv 가능한 방향
    [(0, 1, 2, 3)]  # 5번 cctv 가능한 방향
]

# FUNCTIONS
# 현재 결정하는 cctv의 순번
def init_visited():
    for i in range(N):
        for j in range(M):
            visited[i][j] = False


def in_range(x, y):
    return 0 <= x < N and 0 <= y < M


def make_cases(idx):
    global answer
    if len(cctv_case) == len(cctv_types):
        init_visited()
        for (sx, sy), cctv_type, dir_num in zip(cctv_pos, cctv_types, cctv_case):
            cx, cy = sx, sy
            visited[cx][cy] = True

            for possible_dir in cctvs[cctv_type][dir_num]:
                cx, cy = sx, sy
                dx, dy = dxs[possible_dir], dys[possible_dir]
                while in_range(cx, cy) and grid[cx][cy] != 6:
                    visited[cx][cy] = True
                    cx, cy = cx + dx, cy + dy

        case_answer = 0
        for i in range(N):
            for j in range(M):
                if grid[i][j] != 6 and not visited[i][j]:
                    case_answer += 1
        answer = min(answer, case_answer)

        return
    if idx == len(cctv_types):
        return

    for type in range(len(cctvs[cctv_types[idx]])):
        cctv_case.append(type)
        make_cases(idx + 1)
        cctv_case.pop()


# CODE
N, M = tuple(map(int, input().split()))
answer = sys.maxsize
grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

visited = [
    [False for _ in range(M)]
    for _ in range(N)
]

cctv_pos = []
cctv_types = []
cctv_case = []

# cctv의 위치와 종류를 구한다
for i in range(N):
    for j in range(M):
        if grid[i][j] in {1, 2, 3, 4, 5}:
            cctv_pos.append((i, j))
            cctv_types.append(grid[i][j])

make_cases(0)
print(answer)