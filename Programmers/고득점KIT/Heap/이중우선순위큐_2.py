# 이중우선순위큐
# 프로그래머스의 이중우선순위큐 문제는 TC와 숫자 범위가 적어서 쉽게 통과되는 경향이 있어보였음.
# 백준에 동일한 문제가 있으므로 해당 문제를 통과하는 코드를 짜보려 한다.
# BOJ_7662_이중 우선순위 큐_Gold4

import sys, heapq
read = sys.stdin.readline

for T in range(int(read())):
    # visited[i] --> i번째 삽입된 숫자가 양쪽 우선순위 큐에 존재한다면 True, 한쪽에만 존재하거나 어디에도 존재하지 않는 경우엔 False
    visited = [False] * 1_000_001
    minH, maxH = [], []

    for i in range(int(read())):
        cmd = read().split()

        # 이중 우선순위 큐에 숫자를 삽입해야 하는 경우
        if cmd[0] == 'I':
            heapq.heappush(minH, (int(cmd[1]), i))
            heapq.heappush(maxH, (-int(cmd[1]), i))
            visited[i] = True
        elif cmd[1] == '1':
            while maxH and not visited[maxH[0][1]]:heapq.heappop(maxH)
            if maxH:
                visited[maxH[0][1]] = False
                heapq.heappop(maxH)
        else:
            while minH and not visited[minH[0][1]]:heapq.heappop(minH)
            if minH:
                visited[minH[0][1]] = False
                heapq.heappop(minH)
    while minH and not visited[minH[0][1]]:heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]]:heapq.heappop(maxH)

    if maxH:
        print(-maxH[0][0], minH[0][0])
    else:
        print("EMPTY")



