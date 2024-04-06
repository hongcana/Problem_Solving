import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        if scoville[0] >= K:
            break
            
        if scoville[0] < K and len(scoville) <= 1:
            answer = -1
            break
    
        if scoville[0] < K:
            one = heapq.heappop(scoville)
            two = heapq.heappop(scoville)
            tmp = one + (two * 2)
            heapq.heappush(scoville, tmp)

            answer += 1
            
    return answer