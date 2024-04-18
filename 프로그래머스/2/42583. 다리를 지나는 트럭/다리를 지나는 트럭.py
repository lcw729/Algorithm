def solution(bridge_length, weight, truck_weights):
    answer = 0
    in_bridge = list()
    complete = list()
    
    n = len(truck_weights)
    total = 0
    while len(complete) < n:
                
        # 모든 다리의 시간 카운트
        deprecated = 0
        for idx, truck_info in enumerate(in_bridge):
            time, truck = truck_info
            if time == 1:
                deprecated += 1
                total -= truck
                complete.append(truck)
            else:
                in_bridge[idx][0] = time - 1
        del in_bridge[:deprecated]
                
        if truck_weights:
            result = total + truck_weights[0] # 무게 합산
            if result <= weight and len(in_bridge) < bridge_length:
                in_bridge.append([bridge_length, truck_weights[0]]) # 다리를 지난다.
                truck_weights.pop(0)
                total = result
                    
        answer += 1
            
    return answer