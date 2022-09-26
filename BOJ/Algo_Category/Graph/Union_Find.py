# BOJ 1717
# 각 원소들이 같은 집합에 속해있는지 빠르게 알 수 있는 알고리즘
# Disjoint Set

import sys
si = sys.stdin.readline
sys.setrecursionlimit(10**9)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = tuple(map(int, si().split()))
parent = [i for i in range(n + 1)]

for _ in range(m):
    cmd, a, b = tuple(map(int, si().split()))

    # UNION
    if cmd == 0:
        union(a, b)

    else:
        p1 = find(a)
        p2 = find(b)

        if p1 == p2:
            print("YES")
        else:
            print("NO")
