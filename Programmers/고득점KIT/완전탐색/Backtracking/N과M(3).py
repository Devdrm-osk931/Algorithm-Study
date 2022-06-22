# 중복 순열
n, m = tuple(map(int, input().split()))
result = []


def repetition_permutation(cnt):
    if cnt == m:
        print(*result)
        return

    for i in range(n):
        result.append(i + 1)
        repetition_permutation(cnt + 1)
        result.pop()


repetition_permutation(0)