import heapq
def solution(queries):
    answer = []

    # 플레이어가 매칭 가능한지
    available = dict()

    attack_heap = []
    defense_heap = []
    speed_heap = []


    for query in queries:
        id, attack, defense, speed = query

        # 선수 추가 쿼리
        if id > 0:
            available[id] = True
            heapq.heappush(attack_heap, (-attack, id))
            heapq.heappush(defense_heap, (-defense, id))
            heapq.heappush(speed_heap, (-speed, id))

        # 선수 지목 쿼리
        else:
            # 선수가 없는 경우
            if len(available) == 0:
                answer.append(-1)
            else:
                found = False
                # -1: 공격력, -2: 수비력, -3: 스피드
                if id == -1:
                    while attack_heap:
                        candidate_attack, candidate_id = heapq.heappop(attack_heap)
                        if not available[candidate_id]:
                            continue
                        found = True
                        available[candidate_id] = False
                        answer.append(candidate_id)
                        if found:
                            break
                elif id == -2:
                    while defense_heap:
                        candidate_defense, candidate_id = heapq.heappop(defense_heap)
                        if not available[candidate_id]:
                            continue
                        found = True
                        available[candidate_id] = False
                        answer.append(candidate_id)
                        if found:
                            break
                else:
                    while speed_heap:
                        candidate_speed, candidate_id = heapq.heappop(speed_heap)
                        if not available[candidate_id]:
                            continue
                        found = True
                        available[candidate_id] = False
                        answer.append(candidate_id)
                        if found:
                            break

                if not found:
                    answer.append(-1)


    """
    시간초과 위험
    """
    # players = []

    # for query in queries:
    #     id, attack, defense, speed = query

    #     if id > 0:
    #         players.append(query)
    #         continue

    #     else:
    #         if len(players) == 0:
    #             answer.append(-1)
    #             continue
    #         if id == -1:
    #             players = sorted(players, key=lambda x:x[1])
    #             candidate = players.pop()
    #             answer.append(candidate[0])
    #         elif id == -2:
    #             players = sorted(players, key=lambda x:x[2])
    #             candidate = players.pop()
    #             answer.append(candidate[0])
    #         else:
    #             players = sorted(players, key=lambda x:x[3])
    #             candidate = players.pop()
    #             answer.append(candidate[0])


    return answer