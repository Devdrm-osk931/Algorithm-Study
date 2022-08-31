# BOJ 1269 대칭 차집합

a, b = tuple(map(int, input().split()))
A = set(list(map(int, input().split())))
B = set(list(map(int, input().split())))

x = len(A)
y = len(B)
z = len(A.intersection(B))

print(x + y - 2*z)