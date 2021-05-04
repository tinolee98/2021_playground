# 2021 kakao blind recruit 2번 문제 // combination과 Counter의 조합으로!
# 메뉴 리뉴얼
import sys
from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            comb = list(combinations(sorted(order),c))
            temp += comb
        counter = Counter(temp)
        for f in counter:
            print(f)
        #print(counter)
        #print(counter.values())
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
    return sorted(answer)

orders = ['ABCFG', 'AC', 'CDE', 'ACDE', 'BCFG', 'ACDEH', 'BCA']
course = [2,3,4]
print(solution(orders, course))