def solution(brown, yellow):
    answer = []

    area = brown + yellow;

    for horizontal in range(1, area):
        for vertical in range(1, horizontal + 1):
            if brown == (horizontal + vertical - 2) * 2 and yellow == area - (
                    horizontal + vertical - 2) * 2 and area == horizontal * vertical:
                answer.append(horizontal)
                answer.append(vertical)
                return answer