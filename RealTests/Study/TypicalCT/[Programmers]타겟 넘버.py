def dfs(numbers, target, value):
    if value == target and not numbers:
        return 1
    if not numbers:
        return 0

    cnt = 0
    # number의 첫번째 숫자 더하는 경우
    cnt += dfs(numbers[1:], target, value + numbers[0])
    cnt += dfs(numbers[1:], target, value - numbers[0])

    return cnt


def solution(numbers, target):
    answer = dfs(numbers, target, 0)
    return answer