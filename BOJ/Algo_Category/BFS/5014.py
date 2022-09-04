from collections import deque

f, s, g, u, d = tuple(map(int, input().split()))
dist = [0 for _ in range(f + 1)]
visited = [False for _ in range(f + 1)]


def U(curr):
    return curr + u


def D(curr):
    return curr - d


def in_range(floor):
    return 1 <= floor <= f


def can_go(floor):
    return in_range(floor) and not visited[floor]


cmds = [U, D]
q = deque()

# 시작점 설정(S)
visited[s] = True
dist[s] = 0
q.append(s)

while q:
    curr = q.popleft()
    if curr == g:
        print(dist[curr])
        break

    for cmd in cmds:
        new = cmd(curr)
        if can_go(new):
            visited[new] = True
            dist[new] = dist[curr] + 1
            q.append(new)

if not visited[g]:
    print("use the stairs")