import sys

BLANK = 0
HOUSE = 1
CHICKEN = 2

# 변수 입력
n, m = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

houses = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == HOUSE
]

chickens = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == CHICKEN
]

chickens_cnt = len(chickens)
answer = sys.maxsize
selected = []


def get_chicken_distance():
    global answer
    distance = 0

    for x, y in houses:
        case_min = sys.maxsize
        for i, j in selected:
            case_min = min(case_min, abs(x - i) + abs(y - j))

        distance += case_min
    answer = min(answer, distance)


def solve(idx, cnt):
    if cnt == m:
        get_chicken_distance()
        return
    if idx == chickens_cnt:
        return

    solve(idx + 1, cnt)

    selected.append(chickens[idx])
    solve(idx + 1, cnt + 1)
    selected.pop()


# Main
solve(0, 0)
print(answer)