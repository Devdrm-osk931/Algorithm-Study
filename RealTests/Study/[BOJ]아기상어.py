# BOJ 162236 아기상어
# Samsung Gold3
import sys
from collections import deque


# 변수 및 입력
BLANK = 0
FISH = {1, 2, 3, 4, 5, 6}
SHARK = 9
SIZE = 2
time = 0
catch = 0

N = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

shark_x, shark_y = -1, -1

dist = [
    [-1 for _ in range(N)]
    for _ in range(N)
]
food = []  # 먹을 수 있는 물고기


def init_dist():
    for i in range(N):
        for j in range(N):
            dist[i][j] = -1


# 먹이가 존재하는지 확인한다
def possible():
    global food
    food = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] in FISH and grid[i][j] < SIZE:
                food.append((i, j))
    if len(food) > 0:
        return True
    return False


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def bfs(shark_x, shark_y):
    queue = deque()
    dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
    queue.append((shark_x, shark_y))
    dist[shark_x][shark_y] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and dist[nx][ny] == -1 and grid[nx][ny] <= SIZE:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))


def simulate():
    global shark_x, shark_y, time, catch, SIZE

    while possible():
        # 거리가 작을수록, 행이 작을수록 열이 작을수록
        next_dist, next_x, next_y = sys.maxsize, N + 1, N + 1
        init_dist()

        # 먹이의 위치까지의 거리를 구한다
        bfs(shark_x, shark_y)


        # food에 있는 위치 중 크기가 가장 작은 것을 구한다
        for x, y in food:
            if dist[x][y] == -1:
                continue
            if (next_dist, next_x, next_y) > (dist[x][y], x, y):
                next_dist, next_x, next_y = dist[x][y], x, y

        # 도달할 수 있는 곳이 없다면
        if next_dist == sys.maxsize:
            return

        # food위치까지 이동한다
        grid[shark_x][shark_y] = BLANK
        shark_x, shark_y = next_x, next_y
        grid[shark_x][shark_y] = SHARK

        time += next_dist
        catch += 1

        if catch == SIZE:
            catch = 0
            SIZE += 1


# MAIN
# 초기 위치 찾아주기
for i in range(N):
    for j in range(N):
        if grid[i][j] == SHARK:
            shark_x, shark_y = i, j
simulate()
print(time)