# array 내의 0을 모두 마지막으로 이동시키기

def move_zeros(array):
    count = 0
    while 0 in array:
        count +=1
        print("count")
        array.remove(0)
    for i in range(count):
        array.append(0)
    return array