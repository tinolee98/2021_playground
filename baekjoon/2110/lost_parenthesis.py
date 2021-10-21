lst = list(input())

nums = []
ops = []
temp = ''
for e in lst:
    if e.isdigit():
        temp += e
    else:  
        nums.append(int(temp))
        ops.append(e)
        temp = ''
nums.append(int(temp))
#print(nums)
#print(ops)

if '-' in ops:
    mid = ops.index('-')+1
    result = sum(nums[:mid]) - sum(nums[mid:])
else:
    result = sum(nums)
print(result)