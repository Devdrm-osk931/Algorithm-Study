# BOJ_2644 촌수 계산 실버2

from collections import deque
import sys
INF = sys.maxsize

# 변수 입력
n = int(input())
connections = [
    []
    for _ in range(n + 1)
]
visited = [False for _ in range(n + 1)]
dist = [INF for _ in range(n + 1)]

p1, p2 = tuple(map(int, input().split()))

m = int(input())
for _ in range(m):
    parent, child = tuple(map(int, input().split()))
    connections[parent].append(child)
    connections[child].append(parent)

q = deque()
# BFS 시작점 설정
q.append(p1)
visited[p1] = True
dist[p1] = 0

while q:
    x = q.popleft()
    if x == p2:
        print(dist[p2])
        break
    for next_node in connections[x]:
        if not visited[next_node]:
            visited[next_node] = True
            dist[next_node] = dist[x] + 1
            q.append(next_node)


if dist[p2] == INF:
    print(-1)