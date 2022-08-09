"""
다익스트라 구현방법 공부
1. 인접리스트 이용한 방법
2. 우선순위큐 이용한 방법
"""
import heapq
import sys

N = int(input())  # 도시의 갯수(Vertex)
M = int(input())  # 버스의 갯수(Edge)

graph = [
    []
    for _ in range(N + 1)
]

for _ in range(M):
    a, b, cost = tuple(map(int, input().split()))
    graph[a].append((b, cost))

start, end = tuple(map(int, input().split()))


# Dijkstra by Adjacency List
def getMinNode(dist, visited):
    minVal = sys.maxsize
    minIdx = -1
    for node in range(1, N + 1):
        if dist[node] < minVal and not visited[node]:
            minVal = dist[node]
            minIdx = node
    return minIdx


def listDijkstra(start, end):
    dist = [sys.maxsize] * (N + 1)
    visited = [False] * (N + 1)

    # 시작점에 대한 설정
    dist[start] = 0
    visited[start] = True

    # 시작점에서 도달할 수 있는 지점들에 대한 dist 갱신
    for next_node, cost in graph[start]:
        dist[next_node] = cost

    # N-1번동안 반복
    for _ in range(N + 1):
        min_node = getMinNode(dist, visited)
        visited[min_node] = True
        # dist를 갱신한다 = 기존 dist[j] vs dist[min_node] + dist[min_node][j]
        for node in graph[min_node]:
            dist[node[0]] = min(dist[node[0]], dist[min_node] + node[1])

    # print("visited:", visited)
    # print("dist:", dist)
    return dist[end]

def heapDijkstra(start, end):
    dist = [sys.maxsize] * (N + 1)
    q = []

    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        distance, node = heapq.heappop(q)
        if dist[node] < distance:
            continue
        for next in graph[node]:
            cost = dist[node] + next[1]
            if cost < dist[next[0]]:
                dist[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))


print(listDijkstra(start, end))