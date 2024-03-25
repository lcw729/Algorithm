def solution(record):
    answer = []
    name = {}
    
    for element in record:
        messages = element.split(' ')
        if len(messages) == 3:
            name[messages[1]] = messages[2]
        
    
    for element in record:
        messages = element.split(' ')
        if messages[0] == 'Enter':
            answer.append(name[messages[1]] + '님이 들어왔습니다.')
        elif messages[0] == 'Leave':
            answer.append(name[messages[1]] + '님이 나갔습니다.')
    
    return answer