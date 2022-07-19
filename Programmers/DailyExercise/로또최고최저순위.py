# 2021 Dev-Matching 기출문제

# lottos: 내가 선택한 변호
# win_nums: 정답
def solution(lottos, win_nums):
    answer = []

    correct = 0
    zero = 0

    for lotto in lottos:
        if lotto in win_nums:
            correct += 1
        
        if lotto == 0:
            zero += 1
    
    print(correct)
    print(zero)
    # 최소로 맞춘 경우 - correct 만큼 맞춘 경우
    min_rank = 6 if correct < 2 else (7-correct)

    # 최대로 맞춘 경우 - correct + zero 만큼 맞춘 경우
    max_rank = 6 if (correct + zero) < 2 else (7 - correct - zero)
    
    answer.extend([max_rank, min_rank])

    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))