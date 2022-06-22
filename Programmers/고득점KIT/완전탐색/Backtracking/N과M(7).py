n, m = tuple(map(int, input().split()))
numbers = list(map(int, input().split()))
numbers.sort()
answer = []


def make_permutation(cnt):
    if cnt == m:
        print(*answer)
        return

    for i in range(n):
        answer.append(numbers[i])
        make_permutation(cnt + 1)
        answer.pop()


make_permutation(0)
