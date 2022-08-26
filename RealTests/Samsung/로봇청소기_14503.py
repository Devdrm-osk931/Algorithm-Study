# SAMSUNG 로봇청소기 Gold5
from collections import deque

# N, M, 격자 정보 주어짐
n, m = tuple(map(int, input().split()))

# 로봇 청소기의 위치와 방향 정보
# 북, 동, 남, 서
dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
curr_x, curr_y, curr_dir = tuple(map(int, input().split()))
q = deque()

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False] * m
    for _ in range(n)
]


def count_visited():
    print(len([
        (i, j)
        for i in range(n)
        for j in range(m)
        if visited[i][j]
    ]))


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


# 격자 내에 존재 & 빈 칸 & 청소 x
def can_go(x, y):
    return in_range(x, y) and not grid[x][y] and not visited[x][y]


def move():
    # 첫번째 위치 처리
    visited[curr_x][curr_y] = True
    q.append((curr_x, curr_y, curr_dir))

    while q:
        x, y, dir_num = q.popleft()
        found = False

        # 4 방향을 탐색한다
        for _ in range(4):
            dir_num = (dir_num - 1) % 4
            nx = x + dxs[dir_num]
            ny = y + dys[dir_num]
            if can_go(nx, ny):
                q.append((nx, ny, dir_num))
                visited[nx][ny] = True
                found = True
                break
        if not found:
            # 후진이 가능한지 확인한다
            back_dir = (dir_num - 2) % 4
            nx = x + dxs[back_dir]
            ny = y + dys[back_dir]
            if not grid[nx][ny]:
                q.append((nx, ny, dir_num))
            else:
                return


move()
count_visited()