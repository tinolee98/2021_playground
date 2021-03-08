# N kg 만큼의 설탕을 배달하고자 한다. 이때 사용되는 봉지는 5kg, 3kg 두 종류.
# 가장 적은 개수의 봉지를 이용하려할 때, 사용되는 봉지의 개수는?
# 정확하게 N kg 를 만들 수 없다면 -1을 출력한다.
N = int(input(">> "))
memo = {0:0,1:2, 2:4, 3:1, 4:3}
if N == 4:  # 배달할 수 없는 경우는 오직 4kg 일때만.
    print(-1)
else:
    index = N%5
    num_3 = memo[index]
    num_5 = (N-num_3*3)//5
    print(num_3+num_5)
