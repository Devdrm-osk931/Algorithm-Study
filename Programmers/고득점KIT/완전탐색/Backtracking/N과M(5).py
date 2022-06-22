n, m = tuple(map(int, input().split()))
numbers = list(map(int, input().split()))
numbers.sort()
permutation = []
vst = [False for _ in range(n)]

def make_permutation(cnt):
    if cnt == m:
        print(*permutation)
        return

    for i in range(n):
        if not vst[i]:
            permutation.append(numbers[i])
            vst[i] = True
            make_permutation(cnt + 1)
            vst[i] = False
            permutation.pop()


make_permutation(0)