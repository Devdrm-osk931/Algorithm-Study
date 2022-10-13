# 윷놀이 판 그래프
# 각 점에서 얻을 수 있는 점수, 1번 ~ 5번 움직였을 때 다음 점
# graph = {
#     0: [0, 1, 2, 3, 4, 5],
#     1: [2, 2, 3, 4, 5, 6],
#     2: [4, 3, 4, 5, 6, 7],
#     3: [6, 4, 5, 6, 7, 8],
#     4: [8, 5, 6, 7, 8, 9],
#     5: [10, 21, 22, 23, 24, 25],
#     6: [12, 7, 8, 9, 10, 11],
#     7: [14, 8, 9, 10, 11, 12],
#     8: [16, 9, 10, 11, 12, 13],
#     9: [18, 10, 11, 12, 13, 14],
#     10: [20, 27, 28, 24, 25, 26],
#     11: [22, 12, 13, 14, 15, 16],
#     12: [24, 13, 14, 15, 16, 17],
#     13: [26, 14, 15, 16, 17, 18],
#     14: [28, 15, 16, 17, 18, 19],
#     15: [30, 29, 30, 31, 24, 25],
#     16: [32, 17, 18, 19, 20, 32],
#     17: [34, 18, 19, 20, 32, 32],
#     18: [36, 19, 20, 32, 32, 32],
#     19: [38, 20, 32, 32, 32, 32],
#     20: [40, 32, 32, 32, 32, 32],
#     21: [13, 22, 23, 24, 25, 26],
#     22: [16, 23, 24, 25, 26, 20],
#     23: [19, 24, 25, 26, 20, 32],
#     24: [25, 25, 26, 20, 32, 32],
#     25: [30, 26, 20, 32, 32, 32],
#     26: [35, 20, 32, 32, 32, 32],
#     27: [22, 28, 24, 25, 26, 20],
#     28: [24, 24, 25, 26, 20, 32],
#     29: [28, 30, 31, 24, 25, 26],
#     30: [27, 31, 24, 25, 26, 20],
#     31: [26, 24, 25, 26, 20, 32],
#     32: [0, 32, 32, 32, 32, 32]
# }

graph = [
     [0, 1, 2, 3, 4, 5],
     [2, 2, 3, 4, 5, 6],
     [4, 3, 4, 5, 6, 7],
     [6, 4, 5, 6, 7, 8],
     [8, 5, 6, 7, 8, 9],
     [10, 21, 22, 23, 24, 25],
     [12, 7, 8, 9, 10, 11],
     [14, 8, 9, 10, 11, 12],
     [16, 9, 10, 11, 12, 13],
     [18, 10, 11, 12, 13, 14],
     [20, 27, 28, 24, 25, 26],
     [22, 12, 13, 14, 15, 16],
     [24, 13, 14, 15, 16, 17],
     [26, 14, 15, 16, 17, 18],
     [28, 15, 16, 17, 18, 19],
     [30, 29, 30, 31, 24, 25],
     [32, 17, 18, 19, 20, 32],
     [34, 18, 19, 20, 32, 32],
     [36, 19, 20, 32, 32, 32],
     [38, 20, 32, 32, 32, 32],
     [40, 32, 32, 32, 32, 32],
     [13, 22, 23, 24, 25, 26],
     [16, 23, 24, 25, 26, 20],
     [19, 24, 25, 26, 20, 32],
     [25, 25, 26, 20, 32, 32],
     [30, 26, 20, 32, 32, 32],
     [35, 20, 32, 32, 32, 32],
     [22, 28, 24, 25, 26, 20],
     [24, 24, 25, 26, 20, 32],
     [28, 30, 31, 24, 25, 26],
     [27, 31, 24, 25, 26, 20],
     [26, 24, 25, 26, 20, 32],
     [0, 32, 32, 32, 32, 32]
 ]


move_cnt = list(map(int, input().split()))
case = []
answer = 0


# 말을 선택하는 케이스 모두 생성 -> 1 ~ 4를 10번 고름
def make_case(cnt):
    global answer
    if cnt == 10:
        case_answer = 0
        horse_pos = [0 for _ in range(5)]  # 각 말의 위치 - 초기 모두 0에서 시작
        visited = [False for _ in range(33)]
        for horse_num, move in zip(case, move_cnt):
            curr_pos = horse_pos[horse_num]
            next_pos = graph[curr_pos][move]

            # next_pos가 도착점이 아닌데 이미 다른 말이 있다면 불가능한 케이스
            if next_pos != 32 and visited[next_pos]:
                return

            if curr_pos == 32:
                continue

            # 말을 옮겨준다
            visited[next_pos] = True
            visited[curr_pos] = False
            horse_pos[horse_num] = next_pos
            case_answer += graph[next_pos][0]

        if case_answer > answer:
            answer = case_answer
        return

    for horse in range(1, 5):
        case.append(horse)
        make_case(cnt + 1)
        case.pop()


make_case(0)
print(answer)