def solution(grade):
    answer = 0
    for i in range(len(grade) - 2, -1, -1):
        if grade[i] > grade[i + 1]:
            answer += grade[i] - grade[i + 1]
            grade[i] = grade[i + 1]
    print(grade)
    return answer
