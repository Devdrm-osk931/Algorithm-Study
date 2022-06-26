from collections import deque
import sys

# 두 값이 겹칠 일이 없음 -> visited 관리 필요 x
def fn1(num):
    return num * 2


def fn2(num):
    return int(str(num) + "1")


a, b = tuple(map(int, input().split()))
q = deque()
cmds = [fn1, fn2]

# BFS
ans = 0
q.append((a, 1))

while q:
    x, dist = q.popleft()

    if x == b:
        print(dist)
        sys.exit()

    for cmd in cmds:
        nx = cmd(x)
        if 1 <= nx <= b:
            q.append((nx, dist + 1))


print(-1)