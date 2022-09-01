# BOJ 11478
# 서로 다른 부분 문자열의 개수
# Bactracking & Set
import sys
sys.setrecursionlimit(10**9)
given = list(input())
max_len = len(given)
substring = []
check_set = set()


#idx번째 요소로 시작하는 substring을 만드는 함수
def make_substring(idx):
    if idx == max_len:
        return

    substring.append(given[idx])
    check_set.add("".join(substring))
    # print(substring)
    make_substring(idx + 1)
    substring.pop()


for idx in range(max_len):
    make_substring(idx)

print(len(check_set))