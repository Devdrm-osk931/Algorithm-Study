def solution(word):
    answer = 0
    iterator = ["A", "E", "I", "O", "U"]
    case = []
    cnt = 0

    def dfs(depth):
        nonlocal cnt, answer

        if depth != 0:
            cnt += 1
            if "".join(case) == word:
                answer = cnt
            if depth == 5:
                return

        for i in range(5):
            case.append(iterator[i])
            dfs(depth + 1)
            case.pop()

    dfs(0)

    return answer

print(solution("EIO"))