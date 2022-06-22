n, m = tuple(map(int, input().split()))
numbers = list(map(int, input().split()))
numbers.sort()
combination = []
answers = []


def make_combination(idx, cnt):
    if cnt == m:
        if combination not in answers:
            answers.append(list(combination))
        return
    if idx == n:
        return

    combination.append(numbers[idx])
    make_combination(idx + 1, cnt + 1)
    combination.pop()

    make_combination(idx + 1, cnt)


make_combination(0, 0)
for answer in answers:
    print(*answer)