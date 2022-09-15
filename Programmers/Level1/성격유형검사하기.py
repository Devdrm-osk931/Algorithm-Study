def solution(survey, choices):
    answer = ''

    points = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'J': 0,
        'M': 0,
        'A': 0,
        'N': 0
    }

    criteria = [
        ['R', 'T'],
        ['C', 'F'],
        ['J', 'M'],
        ['A', 'N']
    ]

    for type, level in zip(survey, choices):
        # type의 첫번째 글자가 포인트를 얻는다
        if 1 <= level <= 3:
            points[type[0]] += (4 - level)
        elif level == 4:
            continue

        # type의 두번째 글자가 포인트를 얻는다
        else:
            points[type[1]] += (level - 4)

    for c1, c2 in criteria:
        if points[c1] >= points[c2]:
            answer += c1
        else:
            answer += c2

    return answer