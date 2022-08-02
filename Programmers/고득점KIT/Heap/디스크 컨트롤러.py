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