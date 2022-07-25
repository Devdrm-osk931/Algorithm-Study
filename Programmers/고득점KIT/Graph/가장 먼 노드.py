from collections import deque

def solution(n, edge):
    q = deque()
    answer = 0
    graph = [[] for _ in range(n + 1)]
    distance = [-1 for _ in range(n + 1)]
    
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    
    # 초기설정 - 1번(노드)
    q.append(1)
    distance[1] = 0
    
    while q:
        now = q.popleft()
        
        for next_node in graph[now]:
            if distance[next_node] == -1:
                q.append(next_node)
                distance[next_node] = distance[now] + 1
    
    max_value = max(distance)
    
    for d in distance:
        if d == max_value:
            answer += 1
                
    return answer