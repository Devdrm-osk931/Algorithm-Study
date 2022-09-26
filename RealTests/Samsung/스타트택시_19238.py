# BOJ 스타트택스 19238 골드3
# Samsung
from collections import deque

BLANK = 0
WALL = 1
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


N, M, fuel = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

taxi_x, taxi_y = tuple(map(int, input().split()))
taxi_x, taxi_y = taxi_x - 1, taxi_y - 1

start = [
    [0 for _ in range(N)]
    for _ in range(N)
]

arrive = [-1]

visited = [
    [False for _ in range(N)]
    for _ in range(N)
]

dist = [
    [0 for _ in range(N)]
    for _ in range(N)
]

for i in range(1, M + 1):
    a, b, c, d = tuple(map(int,input().split()))
    start[a - 1][b - 1] = i
    arrive.append((c-1, d-1))


def init():
    for i in range(N):
        for j in range(N):
            visited[i][j] = False
            dist[i][j] = 0


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def bfs(x, y, check):
    start_info = []
    arrive_info = []
    init()
    q = deque()

    q.append((x, y))
    visited[x][y] = True
    dist[x][y] = 0

    while q:
        curr_x, curr_y = q.popleft()

        # 시작점인지 판단
        if start[curr_x][curr_y]:
            start_info.append((dist[curr_x][curr_y], curr_x, curr_y, start[curr_x][curr_y]))

        for dx, dy in zip(dxs, dys):
            nx, ny = curr_x + dx, curr_y + dy
            # 진행이 가능한 곳이라면 진행
            if in_range(nx, ny) and grid[nx][ny] == BLANK and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                dist[nx][ny] = dist[curr_x][curr_y] + 1

    if check:
        start_info.sort()
        arrive_info.sort()

        return start_info[0] if len(start_info) >= 1 else False


def simulate():
    global fuel, taxi_x, taxi_y
    while True:
        # 현재 택시 위치를 기점으로 bfs => 각 출발지까지의 거리를 구한 뒤 그 중 최소값에서 시작을 한다
        curr_x, curr_y = taxi_x, taxi_y
        start_info = bfs(curr_x, curr_y, True)
        if not start_info:
            return True

        s_distance, s_row, s_col, s_num = start_info

        # 출발지까지 이동할만큼 연료가 남아있다면 이동한다
        if fuel >= s_distance:
            taxi_x, taxi_y = s_row, s_col
            fuel -= s_distance

            # 도착지까지의 거리를 구한다
            og_x, og_y = taxi_x, taxi_y
            bfs(taxi_x, taxi_y, False)
            a_row, a_col = arrive[s_num]
            drive_dist = dist[a_row][a_col]

            if drive_dist == 0 and (a_row, a_col) != (og_x, og_y):
                print(-1)
                return False

            if fuel >= drive_dist:
                fuel += drive_dist
                start[s_row][s_col] = 0
                taxi_x, taxi_y = a_row, a_col

            else:
                print(-1)
                return False
        else:
            print(-1)
            return False


def solve():
    for i in range(N):
        for j in range(N):
            if start[i][j]:
                print(-1)
                return

    print(fuel)


possible = simulate()
if possible:
    solve()