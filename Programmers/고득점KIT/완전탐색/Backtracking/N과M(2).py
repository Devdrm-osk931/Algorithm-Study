n, m = tuple(map(int, input().split()))
numbers = [(i + 1) for i in range(n)]
combination = []


def make_combination(cnt, idx):
    if cnt == m:
        print(*combination)
        return
    if idx == n:
        return

    combination.append(numbers[idx])
    make_combination(cnt + 1, idx + 1)
    combination.pop()

    make_combination(cnt, idx + 1)

make_combination(0, 0)