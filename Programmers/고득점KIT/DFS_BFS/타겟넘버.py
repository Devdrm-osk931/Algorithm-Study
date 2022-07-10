answer = 0


def make_comb(numbers, comb, target):
    global answer
    if len(comb) == len(numbers):
        case = 0
        for operation, number in zip(comb, numbers):
            if operation == '+':
                case += number
            else:
                case -= number
        if case == target:
            answer += 1
        return

    for operation in ['+', '-']:
        comb.append(operation)
        make_comb(numbers, comb, target)
        comb.pop()


def solution(numbers, target):
    make_comb(numbers, [], target)

    return answer


print(solution([4, 1, 2, 1], 4))