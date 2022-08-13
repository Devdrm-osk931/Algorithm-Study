# BOJ_Class4_최단경로_Gold4
# 다익스트라 알고리즘 시간 복잡도 --> E log(V)

import heapq
INF = 1e9

 # 정점의 개수(N), 간선의 개수(E)
N, E = tuple(map(int, input().split()))

# 시작점을 입력받는다
start = int(input())

graph = [
    []
    for _ in range(N + 1)
]

for _ in range(E):
    a, b, c = tuple(map(int, input().split()))
    graph[a].append((b, c))

def dijkstra(start):
    Q = []

    dist = [INF] * (N + 1)

    # 시작점 설정
    dist[start] = 0
    heapq.heappush(Q, (0, start))

    while Q:
        # 이전 노드와 연결 된 노드 중 가장 비용이 적은 노드를 고른다
        cost, node = heapq.heappop(Q)

        if dist[node] < cost:
            continue

        for next in graph[node]:
            cost = dist[node] + next[1]

            if dist[next[0]] > cost:
                dist[next[0]] = cost
                heapq.heappush(Q, (cost, next[0]))
    
    return dist[1:]


dists = dijkstra(start)

for dist in dists:
    if dist >= INF:
        print("INF")
    else:
        print(dist)