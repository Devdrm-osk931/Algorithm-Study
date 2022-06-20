def solution(answers):
    MAX_Q = 10_000
    rank = []

    stu1 = [1, 2, 3, 4, 5] * (MAX_Q//5)
    stu2 = [2, 1, 2, 3, 2, 4, 2, 5] * (MAX_Q//8)
    stu3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (MAX_Q//10)

    scores = [0, 0, 0]

    for answer, first, second, third in zip(answers, stu1, stu2, stu3):
        if first == answer:
            scores[0] += 1
        if second == answer:
            scores[1] += 1
        if third == answer:
            scores[2] += 1

    highest = max(scores)
    for idx, score in sorted(enumerate(scores, start=1)):
        if score == highest:
            rank.append(idx)

    return rank
