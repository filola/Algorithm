count = 0

def drf(n, i,numbers, target):
    global count
    
    if i == 0:
        if n == target:
            count +=1
        return 0
    
    drf(n+numbers[0], i-1, numbers[1:],target)
    drf(n-numbers[0], i-1, numbers[1:],target)

def solution(numbers, target):
    answer = count
    drf(0,len(numbers), numbers, target)
    return count