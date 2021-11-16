# This problem is not in Baekjoon.
costs = [[2,4,6,20], [14,2,10,6,12,8]]
outputs = [18,14]

for cost, output in zip(costs, outputs):
    result = 0
    buy = cost[0]
    for i in range(1,len(cost)):
        if cost[i] > buy:
            result += cost[i]-buy
        buy = cost[i]
    print(result)