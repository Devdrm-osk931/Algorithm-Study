def solution(levels):
    answer = 0

    # 주어진 문제들의 난이도를 오름차순으로 정렬한다
    levels.sort()

    # 주어진 문제들 중 상위 25%에 해당하는 문제가 몇개인지 파악한다.
    upper_bound = len(levels)//4

    # 상위 25%에 해당하는 문제가 없다면 -1을 반환한다
    if upper_bound < 1:
        return -1
    
    # 상위 25%에 해당하는 문제가 있다면 해당 문제를 answer로 반환한다
    answer = levels[-upper_bound]

    return answer