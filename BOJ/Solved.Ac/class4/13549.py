"""
On Progress
"""

import heapq, sys
LIMIT = 200_000

# 이동 관련 함수
# 순간이동
def mv1(curr_time, curr_pos):
    return curr_time, curr_pos * 2


# +1
def mv2(curr_time, curr_pos):
    return curr_time + 1, curr_pos + 1


# -1
def mv3(curr_time, curr_pos):
    return curr_time + 1, curr_pos - 1


start, end = tuple(map(int, input().split()))
visited = [False] * (LIMIT + 1)
dist = [sys.maxsize] * (LIMIT + 1)
movements = [mv1, mv2, mv3]
q = []

# 시작점 세팅
visited[start] = True
dist[start] = 0
# 시간, 위치 순으로 큐에 넣어준다
heapq.heappush(q, (0, start))

while q:
    curr_time, curr_pos = heapq.heappop(q)
    if curr_pos == end:
        print(curr_time)
        break
    for mv in movements:
        next_time, next_pos = mv(curr_time, curr_pos)
        if next_pos < 0:
            continue

        if next_pos <= LIMIT and not visited[next_pos]:
            visited[next_pos] = True
            dist[next_pos] = next_time
            heapq.heappush(q, (next_time, next_pos))