import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2:
        s = heapq.heappop(scoville) + (2*heapq.heappop(scoville))
        heapq.heappush(scoville,s)
        count +=1
        if scoville[0] >= K:
            return count
    
    return -1