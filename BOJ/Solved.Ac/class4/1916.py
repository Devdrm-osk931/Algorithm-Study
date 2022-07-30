# BOJ_1916_최소비용 구하기_골드5
# 다익스트라 알고리즘
import sys, heapq
INF = 1e9

si = sys.stdin.readline

n = int(si())
m = int(si())

graph = [
    []
    for _ in range(n + 1)
]

dist = [INF] * (n + 1)

for _ in range(m):
    start, end, cost = tuple(map(int, si().split()))
    graph[start].append((end, cost))

start, target = tuple(map(int, si().split()))

# Dijkstra
q = []
heapq.heappush(q, (0, start))
dist[start] = 0

while q:
    distance, node = heapq.heappop(q)

    if dist[node] < distance:
        continue
    for next in graph[node]:
        cost = dist[node] + next[1]
        if cost < dist[next[0]]:
            dist[next[0]] = cost
            heapq.heappush(q, (cost, next[0]))

print(dist[target])