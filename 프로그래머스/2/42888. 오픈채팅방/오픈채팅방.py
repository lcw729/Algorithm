def solution(record):
    answer = []
    name = {}
    
    for element in record:
        messages = element.split(' ')
        [message, userId] = messages[0], messages[1]
        
        if message == 'Enter':
                name[userId] = messages[2]
                answer.append(userId + '님이 들어왔습니다.')
        elif message == 'Change':
                name[userId] = messages[2]
        elif message == 'Leave':
                answer.append(userId + '님이 나갔습니다.')
    
    for idx, element in enumerate(answer):
        userId = element.split('님')[0]
        answer[idx] = element.replace(userId, name[userId])
    
    return answer