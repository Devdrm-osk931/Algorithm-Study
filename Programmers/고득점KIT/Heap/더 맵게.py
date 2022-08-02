import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        # 모든 요소를 K 보다 크게 만들 수 없는 경우 -1을 반환한다
        if len(scoville) <= 1:
            return -1
        answer += 1
        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1 + (min2 * 2))
    return answer


# TC ==> return 2
print(solution([1, 2, 3, 9, 10, 12], 7))