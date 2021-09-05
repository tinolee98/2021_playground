def solution(nums):
    # 소수 리스트 만들기
    nums.sort()
    max_sum = sum(nums[len(nums)-3:])
    max_sum = min(max_sum, 2997)
    #print(max_sum)
    primes_bools = [False, False,True]
    primes = [2]
    for n in range(3,max_sum+1):
        isPrime = True
        for m in primes:
            if n%m == 0:
                primes_bools.append(False)
                isPrime = False
                break
        if isPrime:
            primes_bools.append(True)
            primes.append(n)
    #print(primes,primes_bools)
    
    # 3개씩 더해보기
    count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1, len(nums)):
                num = nums[i] + nums[j] + nums[k]
                if primes_bools[num]:
                    count += 1
    return count

lst = [[1, 2, 3, 4], [1, 2, 7, 6, 4]]
answer_sheet = []
for item in lst:
    answer_sheet.append(solution(item))

answer = [1,4]
if answer_sheet == answer:
    print("true")
else:
    print("false")