# BOJ_1789_수들의 합_실버5
import math

n = int(input())

ans = (-1 + math.sqrt((1 + 8*n)))/2
print(int(ans))