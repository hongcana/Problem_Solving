from collections import deque

N, bridge_length, weight = map(int, input().split(" "))
truck_weights = list(map(int, input().split(" ")))

time = 0
complete = 0
truck_weights = deque(truck_weights)
while_end_con = sum(truck_weights)

# 다리 길이 만큼 다리 큐를 만든다 
bridge = deque([ 0 for _ in range(bridge_length)])

sum_bridge = 0
while complete != while_end_con:
    
    # 시간 추가
    time += 1
    
    # 다리 위 트럭들 한 칸씩 앞으로 이동
    next = bridge.popleft()
    if next != 0:
        complete += next
        sum_bridge -= next
    
    # 대기 트럭이 있고, 첫 번째 대기 트럭 다리에 더 올라갈 수 있으면
    if (len(truck_weights) >= 1) and (truck_weights[0] + sum_bridge <= weight):
        wei = truck_weights.popleft()
        bridge.append(wei)
        sum_bridge += wei
        
    # 대기 트럭이 없으면
    else:
        bridge.append(0)        

print(time)