# 1 ~ n 까지의 수 중 m 개를 뽑는 방법

n, m = tuple(map(int, input().split()))
permutation = []
visited = [False for _ in range(n)]


def make_permutation(cnt, idx):
    if idx == n:
        if cnt == m:
            print(permutation)
        return

    # idx에 있는 숫자를 뽑는경우
    if not visited[idx]:
        permutation.append(idx + 1)
        visited[idx] = True
        make_permutation(cnt + 1, idx + 1)
        visited[idx] = False
        permutation.pop()

    make_permutation(cnt, idx + 1)

make_permutation(0, 0)


