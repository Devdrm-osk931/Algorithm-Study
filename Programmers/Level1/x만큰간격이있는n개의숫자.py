def solution(x, n):
    answer = []
    num = 0
    for _ in range(n):
        num += x
        answer.append(num)
    return answer