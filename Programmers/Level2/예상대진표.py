# Programmers
# 예상 대진표 Lv2

def solution(n,a,b):
    answer = 1
    a_num, b_num = a, b

    while True:
        a_group, b_group = (a_num + 1) // 2, (b_num + 1) // 2

        if a_group == b_group:
            return answer

        a_num, b_num = (a_num + 1) // 2, (b_num + 1) // 2
        answer += 1


print(solution(8, 4, 7))

# 1 2  3 4  5 6  7 8 --- 1라운드
#  1    3    5    8  --- 2라운드
#    3          8    --- 3라운드
# 같은 그룹에 속할때까지 반복 수행