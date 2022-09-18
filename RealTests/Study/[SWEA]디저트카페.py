# 문제 - SWEA [모의 SW 역량테스트] 디저트카페
# 주소 - https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def possible(i, j, w, h):
    return in_range(i, j) and in_range(i + h, j - h) and in_range(i + h + w, j - h + w) and in_range(i + w, j + w)


def check(i, j, w, h):
    global answer
    move_cnts = [w, h, w, h]
    dxs = [1,  1, -1, -1]
    dys = [1, -1, -1,  1]
    visited = dict()
    case_cnt = 0
    for dx, dy, move_cnt in zip(dxs, dys, move_cnts):
        for _ in range(move_cnt):
            i, j = i + dx, j + dy
            if grid[i][j] not in visited:
                visited[grid[i][j]] = True
                case_cnt += 1
            else:
                return
    answer = max(answer, case_cnt)


def solve():
    # 시작할 점 하나 고르기
    for i in range(N):
        for j in range(N):
            # 대각선 길이 지정 (1 ~ N - 1)
            for w in range(1, N):
                for h in range(1, N):
                    if possible(i, j, w, h):
                        check(i, j, w, h)


# MAIN
TC = int(input())
for tc in range(1, TC + 1):
    answer = -1
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    solve()

    # 답 출력
    print("#%d %d" %(tc, answer))