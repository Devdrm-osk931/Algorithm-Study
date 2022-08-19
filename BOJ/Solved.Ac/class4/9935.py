# BOJ_class4_문자열 폭발_Gold4
# Stack 개념을 사용하는 것이 포인트...
# 하나씩 문자를 추가하면서 타겟과 같은 부분이 발견되면 해당 부분을 삭제해준다.
# 이런식으로 문자열 제거를 진행하면 CC44와 같이 중첩된 형태도 손쉽게 제거할수있다.
# 이제 와서 생각해보니 괄호 문제와도 비슷하다.. 그 문제도 스택을 썼었다
# (( )) 이러한 괄호 쌍들을 알맞게 매칭해줄때도 스택을 썼었다
# 기억하자..😊

characters = input()
target = list(input())
cnt = len(target)

answer = []

for character in characters:
    answer.append(character)

    if answer[-len(target):] == target:
        for _ in range(cnt):
            answer.pop()

if not answer:
    print("FRULA")
else:
    print("".join(answer))