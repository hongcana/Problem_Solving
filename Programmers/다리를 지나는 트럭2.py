from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    
    bridge = deque([ 0 for _ in range(bridge_length)])
    truck_weights = deque(truck_weights)
    
    bridge_sum = 0
    # 대기 트럭 존재 동안 반복
    while truck_weights:
        minus = bridge.popleft()
        bridge_sum -= minus
        
        # 만약 다리에 올라간 트럭들의 무게들의 합 + 다음 트럭의 무게가 무게 제한보다 작다면
        if bridge_sum + truck_weights[0] <= weight:
            top = truck_weights.popleft()
            bridge.append(top)
            
            # 아래처럼 안하고 sum(bridge)를 하면, 최악의 경우 (10000*10000). <- 망함
            bridge_sum += top
        else:
            bridge.append(0)
        time += 1
    
    # 반복 끝나고, 다리의 합이 0이 될 때까지 시간++
    while sum(bridge) != 0:
        bridge.popleft()
        time += 1
    return time