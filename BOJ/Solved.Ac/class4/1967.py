# BOJ_Class4_트리의 지름_Gold4
import heapq

INF = 1e9
N = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b, c = tuple(map(int, input().split()))
    graph[a].append((b, c))

def dijkstra(start):
    Q = []
    dist = [INF] * (N + 1)
    
    # 시작점 setting
    dist[start] = 0
    heapq.heappush(Q, (0, start))
    max_dist = 0

    while Q:
        cost, node = heapq.heappop(Q)

        if dist[node] < cost:
            continue
        
        for next_node, next_cost in graph[node]:
            if dist[next_node] > dist[node] + next_cost:
                dist[next_node] = dist[node] + next_cost
                max_dist = max(max_dist, dist[next_node])
                heapq.heappush(Q, (dist[node] + next_cost, next_node))

    return dist

print(dijkstra(1))
