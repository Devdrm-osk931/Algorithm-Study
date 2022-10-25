# BOJ 1167
# 트리의 지름
from collections import deque
import heapq
INF = 10 ** 9


# 다익스트라
def dijkstra(start):
    q = []
    dist = [INF for _ in range(v + 1)]

    dist[start] = 0
    q.append((0, start))

    while q:
        prev_cost, prev_node = heapq.heappop(q)
        if dist[prev_node] < prev_cost:
            continue
        for next_cost, next_node in graph[prev_node]:
            total = prev_cost + next_cost
            if dist[next_node] > total:
                dist[next_node] = total
                heapq.heappush(q, (total, next_node))

    max_idx, max_distance = -1, -1
    for idx, distance in enumerate(dist):
        if idx == 0:
            continue
        if distance > max_distance:
            max_idx = idx
            max_distance = distance

    return max_idx, max_distance


v = int(input())

graph = {
    i: []
    for i in range(1, v + 1)
}

end_nodes = []

for _ in range(v):
    connection = deque(map(int, input().split()))
    root = connection.popleft()
    cnt = 0

    while connection[0] != -1:
        destination = connection.popleft()
        cost = connection.popleft()

        graph[root].append((cost, destination))


# 임의의 노드에 대해 가장 멀리 떨어져있는 노드를 구한다
n1, d1 = dijkstra(1)

n2, d2 = dijkstra(n1)
print(d2)