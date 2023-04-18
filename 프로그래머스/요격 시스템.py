def solution(targets):
    answer = 0
    point = 0
    targets.sort(key = lambda x:(x[0], x[1]))
    
    for target in targets:
        if target[0] >= point:
            answer += 1
            point = target[1]
        
    return answer

print(solution([[1, 4], [2, 5], [3, 6]]))