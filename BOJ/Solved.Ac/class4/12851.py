# BOJ 12851
# 숨바꼭질2
from collections import deque

MIN, MAX = 0, 100_000
INF = 10 ** 9

n, k = tuple(map(int, input().split()))
dist = [INF for _ in range(MAX + 1)]
visit_cnt = [0 for _ in range(MAX + 1)]


def left(x):
    return x - 1


def right(x):
    return x + 1


def teleport(x):
    return 2*x


def in_range(x):
    return MIN <= x <= MAX

q = deque()

# 움직임 케이스
moves = [left, right, teleport]

# 현재 수빈이의 위치에 대한 정보 입력
dist[n] = 0
visit_cnt[n] += 1
q.append(n)

# BFS
while q:
    x = q.popleft()
    for move in moves:
        nx = move(x)
        # 유효? 범위 내 존재, 현재 점의 거리보다 작거나 같아야함
        if in_range(nx) and dist[nx] >= dist[x] + 1:
            dist[nx] = dist[x] + 1
            visit_cnt[nx] += 1
            q.append(nx)


print(dist[k])
print(visit_cnt[k])
