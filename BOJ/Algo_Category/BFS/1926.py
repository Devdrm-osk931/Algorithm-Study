#BOJ_1926_Silver1
from collections import deque

n, m = tuple(map(int, input().split()))

drawings = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0] * m
    for _ in range(n)
]

drawings_cnt = 0
max_drawing_area = 0

queue = deque()
dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y):
    global max_drawing_area
    cnt = 1
    queue.append((x, y))
    visited[x][y] = cnt

    while queue:
        x, y = queue.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and drawings[nx][ny] == 1 and not visited[nx][ny]:
                cnt += 1
                queue.append((nx, ny))
                visited[nx][ny] = cnt

    max_drawing_area = max(max_drawing_area, cnt)

for row in range(n):
    for col in range(m):
        if drawings[row][col] == 1 and not visited[row][col]:
            drawings_cnt += 1
            bfs(row, col)

print(drawings_cnt)
print(max_drawing_area)
