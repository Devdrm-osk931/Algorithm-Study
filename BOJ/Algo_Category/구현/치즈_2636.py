# BOJ 2636
# 치즈
# Implementation

from collections import deque

n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

temp = [
    [False for _ in range(m)]
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


# 격자 내에 치즈(1)이 존재하지 않으면 완료
def done():
    for r in range(n):
        for c in range(m):
            if grid[r][c] == 1:
                return False
    return True


# 임시 배열 초기화
def init():
    for r in range(n):
        for c in range(m):
            temp[r][c] = False
            visited[r][c] = False


def bfs():
    q = deque()
    i, j = 0, 0  # origin

    visited[i][j] = True
    q.append((i, j))

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[nx][ny] and not grid[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


def get_melting_cheese():
    cnt = 0
    for r in range(n):
        for c in range(m):
            # 치즈에 대해서만 상하좌우 확인
            if not grid[r][c]:
                continue
            adj = 0
            for dx, dy in zip(dxs, dys):
                nx, ny = r + dx, c + dy
                if not in_range(nx, ny):
                    continue
                if not grid[nx][ny] and visited[nx][ny]:
                    adj += 1
            if adj > 0:
                temp[r][c] = True
                cnt += 1
    
    return cnt


def melt():
    for r in range(n):
        for c in range(m):
            if not temp[r][c]:
                continue
            grid[r][c] = 0


def simulate():
    time, cnt = 0, -1
    
    while not done():
        time += 1
        init()  # 초기화 작업
        bfs()  # 치즈 외부 영역을 판별한다

        cnt = get_melting_cheese()  # 녹을 치즈를 표시한다

        melt()  # 치즈를 녹이고 반영한다
    
    print(time)
    print(cnt)


simulate()
