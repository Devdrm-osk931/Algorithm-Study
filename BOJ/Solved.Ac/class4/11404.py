# BOJ_Class4_11404_플로이드_Gold4

INF = 1e9

n = int(input())  # 도시의 갯수
m = int(input())  # 버스의 갯수

graph = [
    [INF for _ in range(n + 1)]
    for _ in range(n + 1)
]


def print_graph():
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(graph[i][j] if graph[i][j] < INF else 0, end=' ')
        print()
    print()


# 자신 -> 자신 = 0으로 초기화
for i in range(n + 1):
    graph[i][i] = 0

# 간선 정보 입력
for _ in range(m):
    a, b, cost = tuple(map(int,input().split()))
    # graph[a][b] 가 처음 초기화 되는 것이라면?
    if graph[a][b] == INF:
        graph[a][b] = cost
    else:
        graph[a][b] = min(graph[a][b], cost)


# Floyd-Warshall Algorithm
def Floyd_Warshall():
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

Floyd_Warshall()
print_graph()
