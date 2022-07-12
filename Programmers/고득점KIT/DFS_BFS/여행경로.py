import collections

answer = []
graph = collections.defaultdict(list)


def dfs(s):
    while graph[s]:
        dfs(graph[s].pop())

    if not graph[s]:
        answer.append(s)
        return


def solution(tickets):
    for a, b in tickets:
        graph[a].append(b)
    for a, b in graph.items():
        graph[a].sort(reverse=True)

    dfs("ICN")

    return answer[::-1]


