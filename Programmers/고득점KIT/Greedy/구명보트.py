from collections import deque


def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)

    min_pointer = 0
    max_pointer = len(people) - 1

    while max_pointer > min_pointer:
        if people[min_pointer] + people[max_pointer] > limit:
            answer += 1
            people.pop()
            max_pointer -= 1
        else:
            people.popleft()
            people.pop()
            answer += 1
            min_pointer = 0
            max_pointer = len(people) - 1
    if people:
        answer += 1

    print(answer)

    return answer

# solution([7, 5, 8, 5], 10)