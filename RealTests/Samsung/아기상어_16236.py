# SAMSUNG 16236
# 아기상어 골드3
import sys
from collections import deque


BLANK = 0
SHARK = 9

n = int(input())
size = 2
catch = 0

time = 0
dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dist = [
    [0 for _ in range(n)]
    for _ in range(n)
]

visited =[
    [False for _ in range(n)]
    for _ in range(n)
]


def init_dist():
    for i in range(n):
        for j in range(n):
            dist[i][j] = 0
            visited[i][j] = False


def possible():
    return any([
        grid[i][j]
        for i in range(n)
        for j in range(n)
        if grid[i][j] != BLANK and grid[i][j] < size
    ])


def get_shark_position():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == SHARK:
                return i, j


# x, y를 시작으로 하는 BFS
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and grid[x][y] <= size


def can_eat(new_x, new_y):
    return grid[new_x][new_y] != BLANK and grid[new_x][new_y] < size


def bfs(x, y):
    global time, size, catch
    candidates = []
    queue = deque()

    # 시작점 설정
    queue.append((x, y))
    dist[x][y] = 0
    visited[x][y] = True

    while queue:
        curr_x, curr_y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = curr_x + dx, curr_y + dy
            if can_go(new_x, new_y):
                dist[new_x][new_y] = dist[curr_x][curr_y] + 1
                visited[new_x][new_y] = True
                queue.append((new_x, new_y))
                if can_eat(new_x, new_y):
                    candidates.append((dist[new_x][new_y], new_x, new_y))

    if not candidates:
        print(time)
        sys.exit()
    else:
        candidates.sort(key=lambda x:(x[0], x[1], x[2]))
        next_x, next_y = candidates[0][1], candidates[0][2]

        # Move Shark & Update Variables
        grid[next_x][next_y] = SHARK
        grid[x][y] = BLANK
        time += candidates[0][0]
        catch += 1

        if catch == size:
            size += 1
            catch = 0
        return


def simulate():
    # 먹을 수 있는 물고기가 있다면
    while possible():
        # BFS를 통해 격자를 탐색하며 가장 먼저 나오는 섭취 가능한 생선을 찾는다
        init_dist()  # BFS를 통한 거리를 기록할 배열을 초기화
        curr_x, curr_y = get_shark_position()
        bfs(curr_x, curr_y)

    print(time)

simulate()