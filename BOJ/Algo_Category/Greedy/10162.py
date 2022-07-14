total_time = int(input())

times = [300, 60, 10]
answers = []

for time in times:
    if time > total_time:
        answers.append(0)
    else:
        if time:
            answers.append(total_time // time)
            total_time = total_time % time

if total_time == 0:
    print(*answers)
else:
    print(-1)

# 더 단순히 10의 배수가 아니라면 -1을 출력
# 각 버튼을 눌러야 할 값을 직접 계산하는게 더 직관적
# 괜히 반복문이랑 조건문을 쓴게 아닌가 싶은 문제