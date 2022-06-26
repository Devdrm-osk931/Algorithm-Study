n, m = tuple(map(int, input().split()))
numbers = list(map(int, input().split()))
numbers.sort()
combination = []
visited = {}


def make_combination(cnt, array):
    if cnt == m:
        if "".join(map(str, combination)) not in visited:
            visited["".join(map(str, combination))] = True
            print(*combination)
        return

    for i in range(len(array)):
        combination.append(array[i])
        make_combination(cnt + 1, array[:i] + array[i+1:])
        combination.pop()


make_combination(0, numbers)