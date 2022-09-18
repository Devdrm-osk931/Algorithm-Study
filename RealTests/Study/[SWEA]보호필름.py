# 문제 - SWEA [모의 SW 역량테스트] 보호필름
# 주소 - https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5V1SYKAaUDFAWu&

def check_col(arr, col):
    cnt = 1

    for row in range(1, d):
        if arr[row][col] == arr[row - 1][col]:
            cnt += 1

        else:
            cnt = 1

        if cnt == k:
            return True

    return False


def check(arr):
    for col in range(w):
        possible = check_col(arr, col)
        if not possible:
            return False
    return True


def solve(depth, idx, limit):
    global answer

    # 보장된 최소 값보다 더 많은 약품처리를 한 경우 cut
    if depth >= answer:
        return

    # limit개의 조합을 고르고 기존 값보다 작은 값 -> 갱신
    if depth == limit:
        if check(film):
            answer = depth
        return

    # 약품 처리 할 행을 고른다
    for row in range(idx, d):
        copy = film[row][:]  # 복구용

        # 해당 열을 모두 0으로 만든다
        for col in range(w):
            film[row][col] = 0

        solve(depth + 1, row + 1, limit)

        for col in range(w):
            film[row][col] = 1

        solve(depth + 1, row + 1, limit)

        for col in range(w):
            film[row][col] = copy[col]


# MAIN
TC = int(input())
for tc in range(1, TC + 1):
    answer = 10 ** 9
    d, w, k = tuple(map(int, input().split()))  # 두께, 가로, 합격기준
    film = [list(map(int, input().split())) for _ in range(d)]

    if check(film):
        # 약품 처리를 안해도 되는 경우
        answer = 0
    else:
        # 조합할 행 갯수를 1 ~ d 개까지 순서대로 늘려가면서 확인
        for limit in range(1, d + 1):
            solve(0, 0, limit)

    print("#%d %d" %(tc, answer))