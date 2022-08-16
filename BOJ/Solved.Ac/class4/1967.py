# BOJ_Class4_트리의 지름_Gold4

# 다익스트라 알고리즘을 이용한 풀이 - 시간초과
"""
import heapq

n = int(input())

# connection
graph = [
    []
    for _ in range(n + 1)
]

tree = {}

for _ in range(n - 1):
    a, b, cost = tuple(map(int, input().split()))
    graph[a].append((b, cost))
    graph[b].append((a, cost))

    if a not in tree:
        tree[a] = [b]
    else:
        tree[a].append(b)

# print(tree)

INF = 1e9
ans = 0
def dijkstra(start):
    dist = [INF] * (n + 1)
    Q = []

    # 시작점 설정
    dist[start] = 0
    heapq.heappush(Q, (0, start))

    while Q:
        curr_cost, curr_node = heapq.heappop(Q)
        for next_node, next_cost in graph[curr_node]:
            total_cost = curr_cost + next_cost
            if dist[next_node] < next_cost:
                continue
            # 갱신 필요가 있다면 갱신한다
            if dist[next_node] > total_cost:
                dist[next_node] = total_cost
                heapq.heappush(Q, (total_cost, next_node))
    
    return max([
        dist[i]
        for i in range(1, n + 1)
    ])

for node in range(1, n + 1):
    if node not in tree:
        ans = max(ans, dijkstra(node))

print(ans)
"""

import heapq

n = int(input())

# connection
graph = [
    []
    for _ in range(n + 1)
]

for _ in range(n - 1):
    a, b, cost = tuple(map(int, input().split()))
    graph[a].append((b, cost))
    graph[b].append((a, cost))


INF = 1e9
ans = 0
def dijkstra(start):
    dist = [INF] * (n + 1)
    Q = []

    # 시작점 설정
    dist[start] = 0
    heapq.heappush(Q, (0, start))

    while Q:
        curr_cost, curr_node = heapq.heappop(Q)
        for next_node, next_cost in graph[curr_node]:
            total_cost = curr_cost + next_cost
            if dist[next_node] < next_cost:
                continue
            # 갱신 필요가 있다면 갱신한다
            if dist[next_node] > total_cost:
                dist[next_node] = total_cost
                heapq.heappush(Q, (total_cost, next_node))
    
    # 거리가 최대인 점의 인덱스와 거리값을 받는다
    max_idx = -1
    max_dist = 0
    for i in range(1, n + 1):
        if dist[i] == INF:
            continue
        
        max_idx = max(max_idx, i)
        max_dist = max(max_dist, dist[i])
    
    return (max_idx, max_dist)

root = 1

# From Root
idx1, dist1 = dijkstra(root)
idx2, dist2 = dijkstra(idx1)
print(dist2)