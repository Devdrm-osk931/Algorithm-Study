import heapq
INF = 10**9
n, e = tuple(map(int, input().split()))
start = int(input())
graph = [
    []
    for _ in range(n + 1)
]

for _ in range(e):
    u, v, w = tuple(map(int, input().split()))
    graph[u].append([v, w])


def dijkstra(start):
    dist = [INF for _ in range(n + 1)]
    print(dist)
    queue = []

    dist[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        curr_dist, curr_node = heapq.heappop(queue)

        for next_node, next_cost in graph[curr_node]:
            new_dist = curr_dist + next_cost

            if dist[next_node] > new_dist:
                dist[next_node] = new_dist
                heapq.heappush(queue, (new_dist, next_node))
    return dist

print(dijkstra(start))