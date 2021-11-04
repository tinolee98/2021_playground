T = int(input())
N = []
for _ in range(T):
    N.append(int(input()))

nums = [1,1,1,2,2]
i = 0
while len(nums) < 100:
    nums.append(nums[i]+nums[i+4])
    i += 1
for n in N:
    print(nums[n-1])