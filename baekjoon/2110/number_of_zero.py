N = int(input())

nums = [i for i in range(1,N+1)]

count2 = 0
count5 = 0

def Count2(n,count):
    if n%2 == 0:
        return Count2(n//2,count+1)
    return count

def Count5(n,count):
    if n%5 == 0:
        return Count5(n//5, count+1)
    return count

for n in nums:
    count2 += Count2(n,0)
    count5 += Count5(n,0)
print(min(count2, count5))