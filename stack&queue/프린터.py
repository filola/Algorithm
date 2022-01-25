from collections import deque

def solution(priorities, location):
    answer = 0
    dec = deque(priorities)
    count = 0
    while True:
        print(dec)
        print(location)
        if dec[0] < max(dec):
          if location == 0:
            location = len(dec)-1
          else:
            location -= 1
          dec.append(dec.popleft())
          
        else:
          dec.popleft()
          location -= 1
          count +=1
        if location < 0:
          break
    return count
print(solution([2, 1, 3, 2],2))