# baekjoon 2869번 문제
import math
u,d,m= map(int,input().split())

day = math.ceil((m-u)/(u-d))

print(day+1)