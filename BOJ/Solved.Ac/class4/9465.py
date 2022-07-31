#BOJ_9465_실버1_스티커
import sys
si = sys.stdin.readline

# 입력받은 TC만큼 확인한다
for _ in range(int(si())):
    column_cnt = int(si())
    stickers = [
        list(map(int, si().split()))
        for _ in range(2)
    ]

    # 열의 갯수가 하나인 경우에는 두 값 중 최대값을 출력한다
    if column_cnt == 1:
        print(max(stickers[0][0], stickers[1][0]))

    else:
        stickers[0][1] = stickers[1][0] + stickers[0][1]
        stickers[1][1] = stickers[0][0] + stickers[1][1]

        for column_index in range(2, column_cnt):
            stickers[0][column_index] = max(stickers[1][column_index - 1], stickers[1][column_index - 2]) + stickers[0][column_index]
            stickers[1][column_index] = max(stickers[0][column_index - 1], stickers[0][column_index - 2]) + stickers[1][column_index]

        print(max(stickers[0][column_cnt - 1], stickers[1][column_cnt - 1]))
