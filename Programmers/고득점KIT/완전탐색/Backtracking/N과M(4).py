# 증가 중복 순열

n, m = tuple(map(int, input().split()))
numbers = [(i + 1) for i in range(n)]
result = []

def make_nondecreasing_permutation(cnt):
    if cnt == m:
        print(*result)
        return

    for i in range(n):
        if len(result) == 0 or numbers[i] >= result[-1]:
            result.append(numbers[i])
            make_nondecreasing_permutation(cnt + 1)
            result.pop()


make_nondecreasing_permutation(0)