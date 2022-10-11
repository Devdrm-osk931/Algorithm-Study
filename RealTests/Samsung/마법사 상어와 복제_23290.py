def init_move_temp():
    for r in range(N):
        for c in range(N):
            move_temp[r][c] = []


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def can_go(x, y):
    return in_range(x, y) and (x, y) != shark and not smell[x][y]


def move_fish():
    # 이동에 쓰일 임시 배열 초기화
    init_move_temp()

    # 물고기를 방향에 따라 이동
    for x in range(N):
        for y in range(N):
            if not copy_temp[x][y]:
                continue
            for curr_dir in copy_temp[x][y]:
                found = False
                for dir_num in range(8):
                    new_dir = (curr_dir + 8 - dir_num) % 8
                    nx, ny = x + dxs[new_dir], y + dys[new_dir]
                    if can_go(nx, ny):
                        move_temp[nx][ny].append(new_dir)
                        found = True
                        break
                if not found:
                    move_temp[x][y].append(curr_dir)

    # move_temp -> copy_temp 반영
    for x in range(N):
        for y in range(N):
            copy_temp[x][y] = move_temp[x][y][:]


# def dfs(x, y, depth, cnt, visit):
#     global max_eat, eat, shark
#     if depth == 3:
#         print(visit)
#         if max_eat < cnt:
#             max_eat = cnt
#             shark = (x, y)
#             eat = visit[:]
#         return
#
#     for d in range(4):
#         nx, ny = x + dx[d], y + dy[d]
#         if in_range(nx, ny):
#             if (nx, ny) not in visit:
#                 visit.append((nx, ny))
#                 dfs(nx, ny, depth + 1, cnt + len(copy_temp[nx][ny]), visit)
#                 visit.pop()
#             else:
#                 dfs(nx, ny, depth + 1, cnt, visit)


def dfs(x, y, depth, cnt, visit):
    global max_eat, eat, shark
    if depth == 3:
        if max_eat < cnt:
            max_eat = cnt
            eat = visit[:]
            shark = x, y

        return
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if in_range(nx, ny) and (nx, ny) not in visit:
            visit.append((nx, ny))
            dfs(x, y, depth + 1, cnt + len(copy_temp[nx][ny]), visit)
            visit.pop()
        else:
            dfs(x, y, depth + 1, cnt, visit)
N = 4
dxs = [0, -1, -1, -1, 0, 1, 1, 1]
dys = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

m, s = tuple(map(int, input().split()))
grid = [[[] for _ in range(N)] for _ in range(N)]
copy_temp = [[[] for _ in range(N)] for _ in range(N)]
move_temp = [[[] for _ in range(N)] for _ in range(N)]
smell = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(m):
    fx, fy, d = tuple(map(int, input().split()))
    grid[fx - 1][fy - 1].append(d - 1)

sx, sy = tuple(map(int, input().split()))
shark = sx - 1, sy - 1

for _ in range(s):
    eat = []
    max_eat = -1

    # 1. 물고기 복제
    for r in range(N):
        for c in range(N):
            copy_temp[r][c] = grid[r][c][:]

    # 2. 물고기 이동
    move_fish()

    # 3. 상어 이동
    dfs(shark[0], shark[1], 0, 0, [])
    for x, y in eat:
        if copy_temp[x][y]:
            copy_temp[x][y] = []
            smell[x][y] = 3

    # 4. 냄새 제거
    for i in range(N):
        for j in range(N):
            if smell[i][j]:
                smell[i][j] -= 1

    # 5. copy_temp를 기존 격자에 복사한다
    for i in range(N):
        for j in range(N):
            grid[i][j] += copy_temp[i][j]


# 최종 물고기 마릿수 구하기
answer = 0
for i in range(N):
    for j in range(N):
        if not grid[i][j]:
            continue
        answer += len(grid[i][j])

print(answer)

