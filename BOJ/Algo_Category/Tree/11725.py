# BOJ_11725_트리의 부모 찾기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

connections = [
    []
    for _ in range(n + 1)
]

parent = {}

for _ in range(n - 1):
    start, end = tuple(map(int, input().split()))
    connections[start].append(end)
    connections[end].append(start)

visited = [False] * (n + 1)

def dfs(node):
    visited[node] = True

    for next in connections[node]:
        if not visited[next]:
            parent[next] = node
            dfs(next)

dfs(1)
for node in range(2, n + 1):
    print(parent[node])