# BOJ_Class4_1504_특정한 최단 경로_Gold4

# 1번 정점 ~ N번 정점까지 최단거리로 이동
# 임의로 주어진 두 정점을 꼭 통과해야함
# 이미 방문한 점을 또 다시 방문해도 됨, 근데 최단거리로 이동해야함 - 만약 최단거리로 이동할 수 없다면 -1을 출력하라

import heapq

N, E = tuple(map(int, input().split()))

graph = [
    []
    for _ in range(N + 1)
]

for _ in range(E):
    a, b, c = tuple(map(int, input().split()))
    graph[a].append((b, c))
    graph[b].append((a, c))

point1, point2 = tuple(map(int, input().split()))

def dijkstra(start):
    INF = 1e9
    Q = []

    dist = [INF] * (N + 1)
    # visited = [False] * (N + 1)

    # 시작점에 대한 처리
    heapq.heappush(Q, (0, start))
    dist[start] = 0

    while Q:
        cost, node = heapq.heappop(Q)

        if dist[node] < cost:
            continue

        for next in graph[node]:
            cost = dist[node] + next[1]
            if dist[next[0]] > cost:
                dist[next[0]] = cost
                heapq.heappush(Q, (cost, next[0]))

    return dist


# 두 케이스 존재
# 1. start -> point1 -> point2 -> end
# 2. start -> point2 -> point1 -> end
start = 1

total = dijkstra(start)
p1 = dijkstra(point1)
p2 = dijkstra(point2)

cnt = min(total[point1] + p1[point2] + p2[N], total[point2] + p2[point1] + p1[N])
print(cnt if cnt < 1e9 else -1)