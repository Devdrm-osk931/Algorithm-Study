# Samsung
# 14889 스타트와 링크 (Silver2)

n = int(input())
synergies = [list(map(int, input().split())) for _ in range(n)]
link = [False for _ in range(n)]

answer = 1e9

def calculate():
    global answer

    start_synergy = sum([
        synergies[i][j]
        for i in range(n)
        for j in range(n)
        if not link[i] and not link[j]
    ])

    link_synergy = sum([
        synergies[i][j]
        for i in range(n)
        for j in range(n)
        if link[i] and link[j]

    ])

    answer = min(answer, abs(start_synergy - link_synergy))


def make_combination(cnt, idx):
    if cnt == n//2:
        calculate()
        return
    
    if idx == n:
        return
    
    # idx를 start팀에 넣는 경우
    make_combination(cnt, idx + 1)

    # idx를 link팀에 넣는 경우
    link[idx] = True
    make_combination(cnt + 1, idx + 1)
    link[idx] = False


make_combination(0, 0)
print(answer)