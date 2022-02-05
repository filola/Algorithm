# baekjoon 2884번 문제
h,m = map(int,input().split())

early = 45

# 1. 빼도 0보다 작아지지 않음
# 2. 뺏을 경우 0보다 작을 경우
# 3. 시간이 0일 경우

if m - early < 0:
    m = 60+(m-early)
    if h == 0:
        h = 23
    else:
        h-=1
else:
    m -= early

print(h,m)
