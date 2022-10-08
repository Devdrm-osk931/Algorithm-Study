def dfs(computer_num, computers, visited, n):
    visited[computer_num] = True

    for j in range(n):
        if computer_num != j and computers[computer_num][j] == 1 and not visited[j]:
            dfs(j, computers, visited, n)
    return visited


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for computer_num in range(n):
        if not visited[computer_num]:
            visited = dfs(computer_num, computers, visited, n)
            answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))