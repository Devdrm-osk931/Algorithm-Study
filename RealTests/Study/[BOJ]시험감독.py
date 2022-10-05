# BOJ 시험감독
# Samsung
import math

N = int(input())  # 시험장 갯수
students = list(map(int, input().split()))  # 각 시험장에 있는 학생 수
main, assist = tuple(map(int, input().split()))  # 총감독관/부감독관

answer = 0
for student in students:
    if student <= main:
        answer += 1

    else:
        answer += 1
        remainder = student - main
        answer += math.ceil(remainder/assist)

print(answer)