# BFS 풀이 - 시간초과
from collections import deque

def solution(n, vertex):
    q = deque()
    map = [
        [0 for _ in range(n + 1)]
        for _ in range(n + 1)
    ]
    
    dist = [
        0 for _ in range(n + 1)
    ]
    
    visited = [
        False for _ in range(n + 1)
    ]
    
    for a, b in vertex:
        map[a][b] = map[b][a] = 1
    

    # 1번 노드 넘버를 큐에 넣는다
    q.append(1)
    visited[1] = True
    
    curr_max = 0
    while q:
        prev_node = q.popleft()
        for next_node in range(1, n + 1):
            if prev_node != next_node and map[prev_node][next_node] and not visited[next_node]:
                q.append(next_node)
                dist[next_node] = dist[prev_node] + 1
                if dist[next_node] > curr_max:
                    curr_max = dist[next_node]
                    cnt = 1
                elif dist[next_node] == curr_max:
                    cnt += 1

                visited[next_node] = True
    
    return cnt

