# Programmers
# 캐시 Lv2

# 캐시의 사이즈가 0인 경우를 체크해주는 것이 중요했다

from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)
    answer = 0

    city_stack = deque()
    city_set = set()

    for city in cities:
        # 존재하지 않는 경우 -> cache_miss!
        if city.lower() not in city_set:
            # stack에 들어있는 도시가 있는 경우
            if city_stack:
                # stack이 가득 차 있는 경우
                if len(city_stack) == cacheSize:
                    # 가장 늦게 사용한 아이템을 삭제한다
                    city_set.remove(city_stack.popleft())

            # city를 stack과 set에 추가한다
            city_stack.append(city.lower())
            city_set.add(city.lower())
            answer += 5

        # 존재하는 경우 -> 순위를 바꿔줘야함
        else:
            # city_stack에서 city를 찾아서 맨 후순위로 밀어줘야함
            city_stack.remove(city.lower())
            city_stack.append(city.lower())
            answer += 1

    return answer

print(solution(0, ["LA", "LA"]))