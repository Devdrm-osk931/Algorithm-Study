import sys

total, win = tuple(map(int, input().split()))
curr_rate = 100 * win // total
answer = sys.maxsize

if curr_rate >= 99:
    print(-1)
else:
    left, right = 1, 1_000_000_000

    while left <= right:
        mid = (left + right) // 2

        # mid 번 이겼을 때 확률을 승률을 구한다
        case_rate = (win + mid) * 100 // (total + mid)

        if case_rate > curr_rate:
            answer = min(answer, mid)
            right = mid - 1
        else:
            left = mid + 1

    print(answer)
