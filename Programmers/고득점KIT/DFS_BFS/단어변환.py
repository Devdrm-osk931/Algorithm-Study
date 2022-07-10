from collections import deque
q = deque()


def diff_cnt(prev_word, next_word):
    cnt = 0
    for i in range(len(prev_word)):
        if prev_word[i] != next_word[i]:
            cnt += 1
    return cnt


def solution(begin, target, words):
    answer = 0

    # target 이 words 리스트에 없는 경우 0을 리턴한다
    if target not in words:
        return 0

    # 각 word에 대해 방문 여부를 확인하는 딕셔너리
    visited = {}
    for word in words:
        visited[word] = False

    # begin -> target by BFS
    q.append((begin, 0))

    while q:
        prev = q.popleft()
        cnt = prev[1]
        prev = prev[0]
        # target 이라면 cnt 값을 출력한다
        if prev == target:
            return cnt

        for word in words:
            # 아직 확인하지 않은 단어임과 동시에 바로 직전 단어와 글자 차이가 단 한개라면 선택
            if not visited[word] and diff_cnt(prev, word) == 1:
                visited[word] = True
                q.append((word, cnt + 1))

    # target word 를 찾지 못했다면 0을 리턴
    return 0
