from collections import deque

def solution(info):
    answer = 0
    sorted_info = sorted(info, key=lambda x: x[0])
    print(sorted_info)
    done = [False for _ in range(len(sorted_info))]

    for i in range(0, len(sorted_info)):
        if not done[i]:
            answer += 1
            acc_sum = sorted_info[i][0]
            done[i] = True
            for j in range(0, len(sorted_info)):
                if not done[j] and sorted_info[j][1] >= acc_sum:
                    done[j] = True
                    acc_sum += sorted_info[j][0]


    return answer

solution([[2, 1], [2, 10], [2, 8]])