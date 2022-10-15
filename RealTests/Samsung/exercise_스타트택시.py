# import
from collections import deque


# 전역변수
BLANK = 0
WALL = 1
IMPOSSIBLE = -1

dxs = [-1, 1, 0, 0]  # 상하좌우 움직임
dys = [0, 0, -1, 1]

INF = 10 ** 9

# 함수
def init():
    for i in range(n):
        for j in range(n):
            visited[i][j] = -1


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# x, y를 시작으로 bfs 수행
def bfs(x, y):
    q = deque()
    visited[x][y] = 0
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and grid[nx][ny] != WALL and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))


def find_nearest_customer():
    x, y, dist = INF, INF, INF
    customer_idx = -1
    found = False
    for customer_num, customer_done in enumerate(done, start = 0):
        if customer_done:
            continue

        # customer_num번째 손님의 위치
        customer_x, customer_y = start[customer_num]

        # 해당 손님이 도달 불가능한 위치에 있다면
        if visited[customer_x][customer_y] == -1:
            continue
        found = True
        if visited[customer_x][customer_y] < dist:
            x, y, dist = customer_x, customer_y, visited[customer_x][customer_y]
            customer_idx = customer_num
        elif visited[customer_x][customer_y] == dist:
            if (x, y) > (customer_x, customer_y):
                x, y, dist = customer_x, customer_y, visited[customer_x][customer_y]
                customer_idx = customer_num

    return x, y, dist, customer_idx, found


def goto_customer_if_possible(nx, ny, nd):
    global tx, ty, fuel

    # nx, ny까지 이동할 연료가 충분한지 확인한다
    if fuel < nd:
        return False

    tx, ty = nx, ny
    fuel -= nd
    return True


def goto_destination_if_possible(customer):
    global tx, ty, fuel
    dx, dy = destination[customer]

    # (nx, ny)가 도달이 가능한 위치인가?
    if visited[dx][dy] == -1:
        return False

    # (nx, ny) 가 도달이 가능하더라도 연료가 충분한가?
    if visited[dx][dy] > fuel:
        return False

    # (nx, ny) 는 도달 가능하고 연료도 충분하다면, 연료를 사용하여 택시를 옮기고, 연료를 채우고 손님을 처리 완료로 바꾼다
    fuel -= visited[dx][dy]
    tx, ty = dx, dy
    done[customer] = True

    fuel += visited[dx][dy] * 2

    return True


def all_done():
    return all([
        done[i]
        for i in range(len(done))
    ])

# 코드
tc = int(input())
for t in range(1, tc + 1):

    # 격자크기, 손님 수, 초기 연료량
    n, m, fuel = tuple(map(int, input().split()))

    # 격자/방문 체크
    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    visited = [
        [-1 for _ in range(n)]
        for _ in range(n)
    ]

    # 택시의 위치
    tx, ty = tuple(map(int, input().split()))
    tx, ty = tx - 1, ty - 1

    # 손님의 시작/끝 위치
    start = []
    destination = []
    done = [False for _ in range(m)]

    for _ in range(m):
        a, b, c, d = tuple(map(int, input().split()))
        start.append((a - 1, b - 1))
        destination.append((c - 1, d - 1))


    while True:

        # 1. BFS를 수행하여 각 점까지의 거리/도달가능 여부를 확인한다
        init()
        bfs(tx, ty)

        # 2. 아직 처리 되지 않은 손님들을 순회
        nx, ny, nd, customer, possible = find_nearest_customer()

        # 도달 가능한 손님이 없다면 종료한다
        if not possible:
            print(f"#{t} {IMPOSSIBLE}")
            break

        possible = goto_customer_if_possible(nx, ny, nd)

        # 최단거리 손님까지 가기에 연료가 부족하다면 종료한다
        if not possible:
            print(f"#{t} {IMPOSSIBLE}")
            break

        # 3. 손님을 태우는 것이 가능하다면 이 지점에서 택시는 손님(customer)를 태웠고, destination[customer] 위치까지 가야함
        init()
        bfs(tx, ty)
        possible = goto_destination_if_possible(customer)

        if not possible:
            print(f"#{t} {IMPOSSIBLE}")
            break

        if all_done():
            print(f"#{t} {fuel}")
            break
