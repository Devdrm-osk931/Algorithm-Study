# N과 M(1)
# 순열(permutation)

n, m = tuple(map(int, input().split()))
numbers = [(i + 1) for i in range(n)]
visited = [False for _ in range(n)]
permutation = []


def make_permutation(cnt):
    if cnt == m:
        print(*permutation)
        return
    for i in range(n):
        if not visited[i]:
            permutation.append(numbers[i])
            visited[i] = True
            make_permutation(cnt + 1)
            permutation.pop()
            visited[i] = False

make_permutation(0)
