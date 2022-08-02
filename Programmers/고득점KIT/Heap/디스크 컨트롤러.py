import heapq

def solution(jobs):
    answer, cnt, start, now = 0, 0, -1, 0
    heap = []
    total = len(jobs)

    while cnt < total:
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, (job[1], job[0]))

        # 선택 가능한 작업이 존재한다면, 소요시간이 가장 짧게 걸리는 작업을 선택하여 진행한다
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            cnt += 1
        else:
            now += 1

    return int(answer/cnt)


print(solution([[0, 3], [1, 9], [2, 6]]))

"""
왜 시간초과가 나는걸까....?
import heapq

def solution(jobs):
    answer = 0
    cnt = 0
    st = -1
    et = 0
    curr_time = 0
    heap = []

    while cnt < len(jobs):
        for job in jobs:
            # -1 ~ 0 사이에 요청 된 작업을 우선순위 큐에 추가해준다 -> 이때 소요시간 기준으로 정렬
            if st < job[0] <= et:
                heapq.heappush(heap, (job[1], job[0]))
        # heap에 요소가 있다면
        if len(heap) > 0:
            curr = heapq.heappop(heap)
            st = et
            et += curr[0]
            curr_time = et
            cnt += 1
            answer += et - curr[1]
        # 현재 시간을 하나 증가시켜준다
        else:
            curr_time += 1

    return int(answer/cnt)


print(solution([[0, 3], [1, 9], [2, 6]]))
"""