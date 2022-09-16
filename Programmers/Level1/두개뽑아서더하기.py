def solution(numbers):
    res_set = set()

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            res = numbers[i] + numbers[j]
            res_set.add(res)
    answer = sorted(list(res_set))
    return answer

print(solution([2,1,3,4,1]))