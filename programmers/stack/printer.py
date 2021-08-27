def solution(priorities, location):
    queue = priorities
    locate = []
    result = []
    for i in range(len(priorities)):
        locate.append(i)
    #print(locate)
    data = queue.pop(0)
    loca = locate.pop(0)
    while (queue):
        maxNum = max(queue)
        if data < maxNum:
            queue.append(data)
            locate.append(loca)
        else:
            result.append(loca)
        data = queue.pop(0)
        loca = locate.pop(0)
        #print(maxNum)
    result.append(loca)
    print(result)
    answer = result.index(location)+1
    return answer