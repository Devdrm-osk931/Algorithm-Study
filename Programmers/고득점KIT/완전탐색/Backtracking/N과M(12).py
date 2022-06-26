n, m = tuple(map(int, input().split()))
numbers = list(map(int, input().split()))
numbers.sort()

visited = {}
combination = []


def answer(cnt, idx):
    if cnt == m:
        if " ".join(map(str, combination)) not in visited:
            visited[" ".join(map(str, combination))] = True
            print(*combination)
        return
    if idx == n:
        return

    for i in range(idx, len(numbers)):
        combination.append(numbers[i])
        answer(cnt + 1, i)
        combination.pop()


answer(0, 0)