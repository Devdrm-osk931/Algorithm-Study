# BOJ 1238
# 파티
import heapq
INF = 10 ** 9
n, m, x = tuple(map(int, input().split()))

graph = {
    i: []
    for i in range(1, n + 1)
}

dist = [
    [INF for _ in range(n + 1)]
    for _ in range(n + 1)
]

for _ in range(m):
    start, end, cost = tuple(map(int, input().split()))
    graph[start].append((cost, end))


def dijkstra(start):
    q = []

    # 시작점 설정
    dist[start][start] = 0
    q.append((0, start))

    while q:
        prev_cost, prev_node = heapq.heappop(q)
        if dist[start][prev_node] < prev_cost:
            continue

        for next_cost, next_node in graph[prev_node]:
            total_cost = prev_cost + next_cost
            if dist[start][next_node] > total_cost:
                dist[start][next_node] = total_cost
                heapq.heappush(q, (total_cost, next_node))


for start_node in range(1, n + 1):
    dijkstra(start_node)

total = [0 for _ in range(n + 1)]

answer = 0
for start_node in range(1, n + 1):
    total[start_node] = dist[start_node][x] + dist[x][start_node]
    answer = max(answer, total[start_node])

print(answer)