# max_sequence function
# arr를 입력받아 arr를 slicing하여 만들 수 있는 subarray 중 sum이 가장 큰 sumarray의 합을 출력하라.
# solution
# 1. arr 내의 가장 큰 element를 찾는다. // 찾을 필요 없이 for문으로 모든 element들을 max로 지정하여 모든 경우를 다 구해서 가장 큰 값을 return하자!
# 2. 해당 element를 기준으로 양쪽으로 탐색을 시작한다.
# 3-1. 탐색한 index의 element가 negative라면 그 값을 value에 저장하고 positive를 탐색할 때까지 3-1을 반복   (index가 커지는 방향 기준)
# 3-2. positive라면 value와 합하였을 때, 그 값이 positive라면 해당 부분까지 subarray에 포함시키고 3번을 다시 반복. // negative라면 value에 저장되었던 모든 element들을 subarray에서 제외 & break
# 4. 양쪽 모두 탐색을 마쳤다면 저장된 subarray의 sum을 return
# Q. the largest element가 하나가 아니라 2개 이상이라면? -> A. 그냥 모든 경우를 다 구해서 가장 큰 값만 return하면 될 거 같아!
arr = list(map(int, input(">> ").split(",")))
if len(arr) == 0 or max(arr) < 0:
    print(0)
result = 0
for max_i in range(len(arr)):
    value = 0
    temp = arr[max_i]
    negative = False
    print(temp)
    for i in range(max_i-1,-1,-1):  # 3-1을 좌측 방향으로 탐색하는 for문
        print(arr[i])
        if arr[i] >= 0: # positive integer를 발견
            if not negative:    # negative integer를 만난 적이 없다면
                temp += arr[i]
                print("not negative!")
            else:   # negative integer를 만났었다면
                if abs(value) <= arr[i]:
                    temp += arr[i] + value
                    print("negative but sum them")
                    value, negative = 0, False  # 조건 초기화
                else:
                    print("break")
                    break   # 더 더하는 것이 의미가 없어짐
        else:
            negative = True
            value += arr[i]
            print("value",value)
    print("temp",temp)
    value = 0
    negative = False
    for i in range(max_i+1,len(arr)):  # 3-1을 우측 방향으로 탐색하는 for문
        print(arr[i])
        if arr[i] >= 0: # positive integer를 발견
            if not negative:    # negative integer를 만난 적이 없다면
                temp += arr[i]
                print("not negative!")
            else:   # negative integer를 만났었다면
                if abs(value) <= arr[i]:
                    temp += arr[i] + value
                    print("negative but sum them")
                    value, negative = 0, False  # 조건 초기화
                else:
                    print("break")
                    break
        else:
            negative = True
            value += arr[i]
            print("value",value)
    if result < temp:
        print("change!")
        result = temp
    print("result",result,"temp",temp)
    print("-----------------------------------------------")
print(result)
