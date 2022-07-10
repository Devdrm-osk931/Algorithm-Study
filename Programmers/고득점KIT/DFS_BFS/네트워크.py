def DFS(computers, stack, visited, n):
    i = stack.pop()
    for j in range(n):
        if j != i and computers[i][j] and not visited[j]:
            visited[j] = True
            stack.append(j)
            DFS(computers, stack, visited, n)

def solution(n, computers):
    answer = 0

    stack = []

    visited = [False for _ in range(n)]

    for i in range(n):
        if not visited[i]:
            stack.append(i)
            visited[i] = True
            DFS(computers, stack, visited, n)
            answer += 1

    return answer