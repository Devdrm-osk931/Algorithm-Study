def solution(routes):
    answer = 0

    routes.sort(key=lambda x: x[1])

    location = -30_001

    for route in routes:
        if route[0] <= location:
            continue

        else:
            location = route[1]
            answer += 1

    return answer

# print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))