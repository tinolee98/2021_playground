N,M = list(map(int, input().split()))
nums = list(map(int,input().split()))
nums.sort()
def Func(size,result,nums,last):
    if size == 0:
        print(' '.join(list(map(str,result[1:]))))
    else:
        for i in range(N):
            if last > nums[i]:
                continue
            result.append(nums[i])
            Func(size-1,result,nums, nums[i])
            result.pop()
Func(M,[0],nums,0)