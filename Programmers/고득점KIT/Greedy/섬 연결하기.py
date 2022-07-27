# Kruskal's Algorithm
def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2])
    routes = set([costs[0][0]])  # 시작점을 0으로 설정

    while len(routes) != n:
        for i, cost in enumerate(costs):
            # 이미 트리에 두 노드가 존재하는데 해당 두개의 노드를 연결하게 되면 사이클이 발생한다
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                answer += cost[2]
                routes.update([cost[0], cost[1]])


    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))