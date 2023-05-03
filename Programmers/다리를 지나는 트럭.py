from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)
    on_bridge = deque([0] * bridge_length)
    
    weights_limit = 0

    while truck_weights:
        now = on_bridge.popleft()
        time += 1
        weights_limit -= now
        
        if weights_limit + truck_weights[0] <= weight:
            tmp = truck_weights.popleft()
            on_bridge.append(tmp)
            weights_limit += tmp
        else:
            on_bridge.append(0)

    while sum(on_bridge) != 0:
        on_bridge.popleft()
        time += 1
    return time