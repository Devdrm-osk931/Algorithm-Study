"""
프로그래머스 Greedy 카테고리 배치된 문제
인터넷에 올라와있는 많은 풀이들은 A가 발견되면 후퇴하는 방식을 채택했으나 반례가 존재한다 - 실제로 해당 풀이들은 현재는 오답으로 처리되고 있음!
완전탐색으로 문제를 해결했는데, 문자열 길이가 최대 20이라 시간초과의 문제가 존재한다
더 좋은 풀이를 고민해봐야할것 같음..
--생각중인 풀이--
1. 쭉 한방향으로 진행
2. 문자열<=20 중 하나의 문자(!= 'A')를 선정
    시작지점부터 선정 문자까지 한방향으로 진행한 뒤, 우회해서 반대방향으로 진행
"""
min_move_sum = 1e9


def count_up_down(character):
    return min(ord(character) - ord('A'), ord('Z') - ord(character) + 1)


def right_left_min(name, curr_idx, next_idx):
    right, left = max(curr_idx, next_idx), min(curr_idx, next_idx)
    right_dist = right - left
    left_dist = left + len(name) - right
    return min(right_dist, left_dist)


def make_permutation(selected, others, name):
    global min_move_sum
    if not others:
        curr_idx = 0
        move_sum = 0
        for next_idx in selected:
            move_sum += right_left_min(name, curr_idx, next_idx)
            curr_idx = next_idx
        # min_move_sum = min(min_move_sum, move_sum)
        min_move_sum = min(min_move_sum, move_sum)
    for i in range(len(others)):
        selected.append(others[i])
        make_permutation(selected, others[:i] + others[i+1:], name)
        selected.pop()


def solution(name):
    alphabet_change_count = 0
    indexes = [idx for idx in range(len(name)) if name[idx] != 'A' and idx != 0]
    for char in name:
        alphabet_change_count += count_up_down(char)
    make_permutation([], indexes, name)
    answer = alphabet_change_count + min_move_sum
    print(alphabet_change_count)
    print(min_move_sum)

    return answer
