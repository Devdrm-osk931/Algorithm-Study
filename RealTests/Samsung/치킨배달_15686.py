import sys

BLANK = 0
HUMAN = 1
HOSPITAL = 2
INF = sys.maxsize


n, m = tuple(map(int, input().split()))
answer = INF

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

humans = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == HUMAN
]

hospitals = [
    (i, j)
    for i in range(n)
    for j in range(n)
    if grid[i][j] == HOSPITAL
]
hospital_cnt = len(hospitals)
selected = []


def compute_minimum():
    global answer
    total_case_dist = 0

    for x, y in humans:
        case_dist = INF
        for i, j in selected:
            case_dist = min(case_dist, abs(x-i) + abs(y-j))
        total_case_dist += case_dist

    answer = min(answer, total_case_dist)


# 병원 중 m개의 병원을 선택하는 방법
def solve(curr_idx, cnt):
    if cnt == m:
        compute_minimum()
        return
    if curr_idx == hospital_cnt:
        return

    solve(curr_idx + 1, cnt)

    selected.append(hospitals[curr_idx])
    solve(curr_idx + 1, cnt + 1)
    selected.pop()


solve(0, 0)
print(answer)