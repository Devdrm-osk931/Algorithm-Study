# 유니온파인드
import sys
si = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


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
    a, b, c = tuple(map(int, si().split()))

    if not a:
        union(b, c)
    else:
        b = find(b)
        c = find(c)
        if b == c:
            print("YES")
        else:
            print("NO")