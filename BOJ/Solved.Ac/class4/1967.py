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

# 위 알고리즘을 개선하여 결국 최대 지점은 Leaf node 중 하나에서 있을 것이라고 생각하여 리프노드에서만 진행했지만 해당 알고리즘도
# O(n^2logn) 시간복잡도를 갖게 되어 시간초과가 나는 것 같다
# 트리의 경우 특정 노드를 재방문하여 최단거리가 갱신되는 경우가 발생하지 않기 때문에, dfs/bfs를 사용하여 O(n) 안에 해결이 가능하다.

# Solution - O(n)
# 연결리스트를 이용한 dfs -> O(n)
import sys
from collections import deque

si = sys.stdin.readline

n = int(si())

graph = [
    []
    for _ in range(n + 1)
]

for _ in range(n - 1):
    a, b, cost = tuple(map(int, si().split()))
    graph[a].append((b, cost))
    graph[b].append((a, cost))


def bfs(root):
    max_dist, max_idx = 0, -1
    dist = [0] * (n + 1)
    visited = [False] * (n + 1)
    q = deque()

    q.append(root)
    dist[root] = 0
    visited[root] = True

    while q:
        prev_node = q.popleft()
        for next_node, next_cost in graph[prev_node]:
            if not visited[next_node]:
                dist[next_node] = dist[prev_node] + next_cost
                visited[next_node] = True
                q.append(next_node)

    for i in range(1, n + 1):
        if dist[i] > max_dist:
            max_dist = dist[i]
            max_idx = i

    return max_idx, max_dist


root = 1
f_idx, f_dist = bfs(root)
print(bfs(f_idx)[1])