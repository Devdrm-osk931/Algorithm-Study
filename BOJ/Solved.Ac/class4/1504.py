# BOJ_Class4_1504_특정한 최단 경로_Gold4

# 1번 정점 ~ N번 정점까지 최단거리로 이동
# 임의로 주어진 두 정점을 꼭 통과해야함
# 이미 방문한 점을 또 다시 방문해도 됨, 근데 최단거리로 이동해야함 - 만약 최단거리로 이동할 수 없다면 -1을 출력하라

# 다시 보기
import heapq

N, E = tuple(map(int, input().split()))

graph = [
    []
    for _ in range(N + 1)
]

for _ in range(E):
    a, b, cost = tuple(map(int, input().split()))
    graph[a].append((b, cost))
    graph[b].append((a, cost))

p1, p2 = tuple(map(int, input().split()))


INF = 1e9
def dijkstra(start):
    Q = []
    dist = [INF] * (N + 1)

    # 시작점 거리 처리 후 Q에 넣어줌
    dist[start] = 0
    heapq.heappush(Q, (0, start))

    while Q:
        # 최소 비용으로 선택된 다음 지점
        cost, node = heapq.heappop(Q)
        
        # dist[node] 가 cost 보다 작은 경우는 고려하지 않아도 된다
        if dist[node] < cost:
            continue

        # node 를 거쳐 next_node 로 가는것이 더 이득이라면 dist를 갱신해준다
        for next_node, next_cost in graph[node]:
            if dist[next_node] > dist[node] + next_cost:
                dist[next_node] = dist[node] + next_cost
                heapq.heappush(Q, (dist[node] + next_cost, next_node))

    return dist

# p1, p2 를 거쳐가는 최단거리?
# 1. start -> p1 -> p2 -> N
# 2. start -> p2 -> p1 -> N
start, end = 1, N
case1 = dijkstra(start)
case2 = dijkstra(p1)
case3 = dijkstra(p2)

ans = min(case1[p1] + case2[p2] + case3[N], case1[p2] + case3[p1] + case2[N])

if ans < INF:
    print(ans)
else:
    print(-1)