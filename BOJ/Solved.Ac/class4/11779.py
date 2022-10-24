# BOJ 11779
# 최소비용 구하기2
import sys, heapq
input = sys.stdin.readline

INF = 10 ** 9


def dijkstra(start):
    q = []

    dist[start] = 0
    prev[start] = start
    heapq.heappush(q, (0, start))

    while q:
        prev_cost, prev_node = heapq.heappop(q)
        if dist[prev_node] < prev_cost:
            continue
        for next_cost, next_node in graph[prev_node]:
            total_cost = dist[prev_node] + next_cost
            if total_cost < dist[next_node]:
                heapq.heappush(q, (total_cost, next_node))
                dist[next_node] = total_cost
                prev[next_node] = prev_node


n = int(input())
m = int(input())

graph = {
    i: []
    for i in range(1, n + 1)
}

for _ in range(m):
    s, e, cost = tuple(map(int, input().split()))
    graph[s].append((cost, e))

s, e = tuple(map(int, input().split()))
dist = [INF for _ in range(n + 1)]
prev = [-1 for _ in range(n + 1)]

dijkstra(s)

route = []
length = 0
idx = e
route.append(e)
length += 1
while idx != s:
    idx = prev[idx]
    route.append(idx)
    length += 1

print(dist[e])
print(length)
print(*route[::-1])