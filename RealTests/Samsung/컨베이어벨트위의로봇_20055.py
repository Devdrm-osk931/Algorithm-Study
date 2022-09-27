# Samsung BOJ Gold4
# 컨베이어 벨트 위의 로봇

N, K = tuple(map(int, input().split()))
durability = list(map(int, input().split()))
robots = [False for _ in range(2 * N)]


def rotate_right(arr: list):
    tmp = arr[-1]
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = tmp


# 시뮬레이션
def simulate():
    answer = 0
    while True:
        answer += 1
        # Step1: 벨트가 각 칸 위의 로봇과 함께 한 칸 회전한다
        rotate_right(durability)
        rotate_right(robots)

        # 내리는 위치에 로봇이 있다면 로봇을 내려준다
        if robots[N - 1]:
            robots[N - 1] = False

        # Step2: 가장 먼저 올라간 로봇부터, 벨트가 회전하는 방향으로 이동
        for i in range(2*N - 1, -1, -1):
            if robots[i]:
                next_idx = (i + 1) % (2 * N)

                # 다음 위치에 로봇이 없고 내구도가 1 이상이라면 이동이 가능하다
                if not robots[next_idx] and durability[next_idx] >= 1:
                    robots[i] = False
                    robots[next_idx] = True
                    durability[next_idx] -= 1

                    # 내리는 위치에 로봇이 있다면 로봇을 내려준다
                    if robots[N - 1]:
                        robots[N - 1] = False

        # Step3: 올리는 위치에 내구도가 0이 아니면 올리는 위치에 로봇을 올린다
        if not robots[0] and durability[0] > 0:
            robots[0] = True
            durability[0] -= 1

        # Step4: 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다
        zero_cnt = len([True for i in range(2*N) if durability[i] == 0])
        if zero_cnt >= K:
            return answer


print(simulate())