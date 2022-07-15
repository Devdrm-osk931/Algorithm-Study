# Programmers_Daily Exercise
# 2022 KAKAO BLIND RECRUITMENT 신고결과받기

def solution(id_list, report, k):
    answer = []
    reply_cnt = {}
    reported_reporter_map = {}

    for id in id_list:
        reply_cnt[id] = 0

    for single_report in report:
        reporter, reported = single_report.split()
        if reported not in reported_reporter_map:
            reported_reporter_map[reported] = {reporter}
        else:
            reported_reporter_map[reported].add(reporter)
    
    for reported, reporter_set in reported_reporter_map.items():
        if len(reporter_set) >= k:
            for reporter in reporter_set:
                reply_cnt[reporter] += 1
        
    
    return list(reply_cnt.values())


ex_id_list = ["muzi", "frodo", "apeach", "neo"]
ex_report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
ex_report2 = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi", "muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
ex_k = 2

print(solution(ex_id_list, ex_report, ex_k))
print(solution(ex_id_list, ex_report2, ex_k))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))