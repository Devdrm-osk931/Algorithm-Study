# Programmers LV1
# 2020 카카오 인턴십_키패드 누르기

def solution(numbers, hand):
    answer = ''

    # 숫자들의 격자 내 위치를 나타내는 배열을 만든다
    num_pos = [(-1, -1)] + [
        (i, j)
        for i in range(1, 4)
        for j in range(1, 4)
    ] + [(4, 2)]

    l_pos = (4, 1)
    r_pos = (4, 3)

    def compare_dist(anum_pos, lpos, rpos):
        ldist = abs(anum_pos[0] - lpos[0]) + abs(anum_pos[1] - lpos[1])
        rdist = abs(anum_pos[0] - rpos[0]) + abs(anum_pos[1] - rpos[1])

        if ldist>rdist:
            return 'R'
        elif ldist < rdist:
            return 'L'
        else:
            return 'S'

    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            l_pos = num_pos[number]
        
        elif number in [3, 6, 9]:
            answer += 'R'
            r_pos = num_pos[number]

        else:
            # 주어진 숫자와 현재 손가락 위치를 비교한다
            if number == 0:
                anum_pos = num_pos[10]
            else:
                anum_pos = num_pos[number]
            
            comp = compare_dist(anum_pos, l_pos, r_pos)

            if comp == 'L':
                answer += 'L'
                l_pos = anum_pos
            
            elif comp == 'R':
                answer += 'R'
                r_pos = anum_pos

            else:
                if hand == 'right':
                    answer += 'R'
                    r_pos = anum_pos
                else:
                    answer += 'L'
                    l_pos= anum_pos

    print(answer)
    return answer


tc1 = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
print(tc1 == "LRLLLRLLRRL")

tc2 = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")
print(tc2 == "LRLLRRLLLRR")

tc3 = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")
print(tc3 == "LLRLLRLLRL")