# BOJ_Class4_1043거짓말
from collections import deque

n, m = tuple(map(int, input().split()))  # 사람 수 & 파티 수

# 진실을 아는 사람의 수, 사람에 대한 정보
truth = list(map(int, input().split()))
truth_cnt = truth[0]
if truth_cnt >= 1:
    truth_list = set(truth[1:])
else:
    truth_list = set()

# 각 파티에 참석한 사람들에 관한 정보를 담는 리스트
party_participants = []

for _ in range(m):
    participants = set(list(map(int, input().split()))[1:])
    party_participants.append(participants)

# DFS를 통해 구해보자
visited = [False] * (1 + n)
stack = []
for elem in truth_list:
    stack.append(elem)
    visited[elem] = True

def dfs():
    while stack:
        now = stack.pop()
        for party in party_participants:
            if now in party:
                for person in party:
                    if not visited[person]:
                        stack.append(person)
                        visited[person] = True

dfs()

answer = 0
for party in party_participants:
    flag = False  #진실을 아는 사람이 있는지 확인
    for person in party:
        if visited[person]:
            flag = True
            break
    # 진실을 아는 사람이 한명도 없는 경우엔 과장해도 된다
    if not flag:
        answer += 1

print(answer)
