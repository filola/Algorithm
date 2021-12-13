def solution(progresses, speeds):
    answer = []

    while True:
        count = 0
        finish = []
        if not progresses:
            break
            
        if progresses[0] >= 100:
            for num in range(len(progresses)):
                if progresses[num] < 100:
                  break
                finish.append(num)   
                count += 1
          
            answer.append(count)
            
            for i in finish[-1::-1]:
              progresses.pop(i)

        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        print(progresses)
            
    return answer

print(solution([96, 94],[3,3]))