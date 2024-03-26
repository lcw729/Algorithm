def solution(participant, completion):
    answer = ''
    people = {}
    
    for name in participant:
        if name in people:
            people[name] += 1
        else:
            people[name] = 1
    
    for name in completion:
        if people[name] == 1:
            del people[name]
        else:
            people[name] -= 1
    
    
    return list(people.keys())[0]