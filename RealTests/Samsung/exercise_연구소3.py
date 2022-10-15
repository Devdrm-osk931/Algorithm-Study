# Import
import sys
from collections import deque

# Global Var
BLANK = 0
WALL = 1
VIRUS = 2
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


# Functions
def get_virus():
    virus = [
        (i, j)
        for i in range(n)
        for j in range(n)
        if grid[i][j] == VIRUS
    ]
    return virus


def init():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            dist[i][j] = 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def possible():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == BLANK and visited[i][j] == False:
                return False
    return True


def bfs(check):
    global answer

    q = deque()
    init()

    for x, y in check:
        visited[x][y] = True
        dist[x][y] = 0
        q.append((x, y))

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] != WALL:
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

    # 벽이 아닌 모든 칸에 바이러스가 퍼져있는지 확인
    if possible():
        global answer
        x = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == BLANK:
                    x = max(x, dist[i][j])

        answer = min(answer, x)

def solve(cnt, idx):
    if cnt == m:
        bfs(check)
        return

    if idx == len(virus):
        return

    # idx 번째를 뽑을때
    check.append(virus[idx])
    solve(cnt + 1, idx + 1)
    check.pop()

    # idx 번째를 뽑지 않을 때
    solve(cnt, idx + 1)


# Main
tc = int(input())
for t in range(tc):
    n, m = tuple(map(int, input().split()))
    check = []
    answer = sys.maxsize

    # 0은 벽, 2는 바이러스를 놓을 수 있는 위치
    grid = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    visited = [
        [False for _ in range(n)]
        for _ in range(n)
    ]

    dist = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    virus = get_virus()

    solve(0, 0)
    if answer == sys.maxsize:
        print(f"#{t + 1} %d" %(-1))
    else:
        print(f"#{t + 1} {answer}")

"""
7
7 3
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 0 0 2
7 3
2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
7 4
2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
7 5
2 0 2 0 1 1 0
0 0 1 0 1 2 0
0 1 1 2 1 0 0
2 1 0 0 0 0 2
0 0 0 2 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
7 3
2 0 2 0 1 1 0
0 0 1 0 1 0 0
0 1 1 1 1 0 0
2 1 0 0 0 0 2
1 0 0 0 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
7 2
2 0 2 0 1 1 0
0 0 1 0 1 0 0
0 1 1 1 1 0 0
2 1 0 0 0 0 2
1 0 0 0 0 1 1
0 1 0 0 0 0 0
2 1 0 0 2 0 2
5 1
2 2 2 1 1
2 1 1 1 1
2 1 1 1 1
2 1 1 1 1
2 2 2 1 1
"""