# BOJ 14938
# 서강 그라운드
import heapq

INF = 10 ** 9

# 입력
n, m, r = tuple(map(int, input().split()))
items = list(map(int, input().split()))

graph = [
    []
    for _ in range(n + 1)
]

dist = [INF for _ in range(n + 1)]

for _ in range(r):
    a, b, cost = tuple(map(int, input().split()))
    graph[a].append((cost, b))
    graph[b].append((cost, a))


def dijkstra(start):
    global dist, answer
    # dist 배열 초기화, 우선순위큐 생성
    dist = [INF for _ in range(n + 1)]
    q = []
    case_answer = 0

    # 시작점 처리
    dist[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        curr_dist, curr_node = heapq.heappop(q)
        if dist[curr_node] < curr_dist:
            continue

        for next_cost, next_node in graph[curr_node]:
            total_cost = dist[curr_node] + next_cost
            if dist[next_node] > total_cost:
                dist[next_node] = total_cost
                heapq.heappush(q, (total_cost, next_node))

    for i in range(1, n + 1):
        if dist[i] <= m:
            case_answer += items[i - 1]

    answer = max(answer, case_answer)


answer = 0
for node in range(1, n + 1):
    dijkstra(node)
print(answer)
