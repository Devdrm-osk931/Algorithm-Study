# 배열에서 첫번째 요소보다 더 높은 우선순위를 가진것이 있는지 확인한다
def check_most_priority(priorities):
    for idx in range(1, len(priorities)):
        if priorities[idx] > priorities[0]:
            return False
    return True

def solution(priorities, location):
    answer = 0  # 몇번째 출력인지 확인
    curr = location

    while len(priorities) > 0:
        # 첫번째 요소가 제일 우선순위가 높은지 확인
        if check_most_priority(priorities):
            # 현재 최우선 순위가 타겟 작업이라면
            if curr == 0:
                answer += 1
                return answer
            else:
                priorities.pop(0)
                curr = (curr - 1 + len(priorities)) % len(priorities)
                answer += 1

        # 첫번째 요소를 맨 뒤로 보낸 뒤 타겟 아이템의 인덱스 업데이트
        else:
            popped_item = priorities.pop(0)
            priorities.append(popped_item)
            curr = (curr - 1 + len(priorities)) % len(priorities)


