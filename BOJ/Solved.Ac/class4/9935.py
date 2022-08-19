# BOJ_class4_문자열 폭발_Gold4

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