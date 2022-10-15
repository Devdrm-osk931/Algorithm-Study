arr = [1, 2, 3, 4]

case = []
visited = [False, False, False, False]


def permuation(cnt):
    if cnt == 4:
        print(case)
        return

    for i in range(4):
        if not visited[i]:
            visited[i] = True
            case.append(arr[i])
            permuation(cnt + 1)
            case.pop()
            visited[i] = False

def combination(idx, cnt):
    if cnt == 3:
        print(case)
        return
    if idx == len(arr):
        return

    case.append(arr[idx])
    combination(idx + 1, cnt + 1)
    case.pop()

    combination(idx + 1, cnt)

combination(0, 0)