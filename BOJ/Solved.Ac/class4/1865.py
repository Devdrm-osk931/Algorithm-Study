import sys
si = sys.stdin.readline
INF = 10 ** 9

# 벨만포드 알고리즘
def bf(start):
    dist[start] = 0

    # n번 진행
    for rep in range(1, n + 1):
        for curr in range(1, n + 1):
            for next, time in graph[curr]:
                if dist[next] > dist[curr] + time:
                    dist[next] = dist[curr] + time
                    # 만약 n번째 반복에서 갱신이 된다면 음수 사이클이 존재하는것이다
                    if rep == n:
                        return True
    return False


tc = int(si())
for _ in range(tc):
    n, m, w = tuple(map(int, si().split()))
    dist = [INF for _ in range(n + 1)]

    graph = {
        i: []
        for i in range(1, n + 1)
    }

    for _ in range(m):
        s, e, t = tuple(map(int, si().split()))
        graph[s].append((e, t))
        graph[e].append((s, t))

    for _ in range(w):
        s, e, t = tuple(map(int, si().split()))
        graph[s].append((e, -t))

    if bf(1):
        print("YES")
    else:
        print("NO")