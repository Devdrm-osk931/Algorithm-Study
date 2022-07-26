from collections import deque

def solution(n, wires):
    answer = 1e9

    # connection 중 하나씩 끊어가며 각 그룹의 포함된 노드 갯수의 차이를 answer에 넣어가며 최소값을 리턴한다
    for i in range(len(wires)):
        q = deque()

        case_connection = [
            wires[k] for k in range(len(wires)) if k != i
        ]

        graph = [
            [] for _ in range(n + 1)
        ]

        for a, b in case_connection:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False for _ in range(n + 1)]

        # 연결을 한개 끊었을 때 두 그룹이 몇개의 노드로 구성되었는지 담고 있는 배열
        how_many = []
        for node in range(1, n + 1):
            if not visited[node]:

                q.append(node)
                visited[node] = True
                cnt = 1

                while q:
                    now = q.popleft()
                    for next in graph[now]:
                        if not visited[next]:
                            q.append(next)
                            visited[next] = True
                            cnt += 1

                how_many.append(cnt)
        diff = abs(how_many[0] - how_many[1])
        answer = min(answer, diff)

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))