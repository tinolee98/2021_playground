arr = list(map(int, input(">> ").split(",")))
max,curr=0,0
for x in arr:
    curr+=x
    if curr<0:curr=0
    if curr>max:max=curr
print(max)

# 앞에서부터 element를 하나씩 더해가는데, curr<0 이라면 버리는 게 낫다고 판단할 수 있음.
# curr > max: max = curr 를 통해 만약 negative를 만나 curr이 작아지더라도 max 값은 변하지 않고
# 큰 postive를 만나 curr이 커진다면 max를 갱신하여 항상 최대값이 저장되고 최종적으로 출력될 수 있음.